import asyncio
from doctest import debug
from hmac import new
from os import name
import re
from tkinter import N
from turtle import mode, up
from venv import create
from numpy import rec, where
from prisma import Prisma, types, models
from fastapi import FastAPI, HTTPException
import json
import pandas as pd
from FoodRecommender import FoodRecommender
from FoodRecommender import createRecommendations
from import_recipes import import_recipes
from import_ingredients import import_ingredient
from import_instructions import import_instruction
from prisma.partials import RECIPESWithoutId
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

mod_path = Path(__file__).parent

origins = [
    "*"
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/recipes/update/{id}",  response_model=models.RECIPES)
async def update(recipe:  dict , id: int):
    # db = Prisma()
    # await db.connect()
    # updated_recipe_input = types.RECIPESUpdateInput(**json.loads(recipe.json()))
    # updated_recipe = await db.recipes.update(
    # where={
    #     'id': id,
    # },
    # data=updated_recipe_input,
    # )
    # await db.disconnect()
    recipe['id'] = id
    updated_recipe = await import_recipes(recipe, output_id=True, debug=True, verbose=True)
    return updated_recipe

@app.post("/recipes/delete/{recipe_id}")
async def delete(recipe_id: int):
    db = Prisma()
    await db.connect()
    recipe = await db.recipes.delete(
        where={'id': recipe_id}
    )
    await db.disconnect()
    return recipe

def list_recipes_to_json_df(found):
    found_json = "["
    for recipe in found:
        # found.__dict__
        found_json += f'{recipe.json()},'
    found_json = found_json[:-1] + "]"
    df = pd.read_json(found_json)
    return found_json,df


def prettifyJson(jsonString):
    parsed = json.loads(jsonString)
    return json.dumps(parsed, indent=4)

#uvicorn main:app --reload
@app.get("/")
async def root():
    db = Prisma()
    await db.connect()
    found = await db.recipes.find_many(where={
        'OR' : [
            {'id': 1},
            {'id': 27},
            {'id': 868}
            ]
        }
    )

    await db.disconnect()

    if found.__len__() > 0:
        found_json, df = list_recipes_to_json_df(found)
        print(df.head())
    else:
        found_json = "[]"
    return found_json
    # convert found : List[RECPIES] to json
    # found_json = []
    # for recipe in found:
        # print(f'found recipe: {recipe.json(indent=2)}')
    # if found is not None:
    #     found_json, df = list_recipes_to_json_df(found)
        # print(df.head())
    # else:
    #     found_json = "[]"
    return found_json

@app.get("/search/{keyword}", response_model=list[models.RECIPES])
async def recipebyKeyword(keyword: str):
    db = Prisma()
    await db.connect()
    found = await db.recipes.find_many(
        where={
            "name": {
                "contains" : keyword,
                "mode": "insensitive"
            }
        }
    )  
    await db.disconnect()
    return found


@app.get("/search/{keyword}/{sorting}",response_model=list[models.RECIPES])
async def recipesbyKeywordWithSorting(keyword: str, sorting: models.fields.LiteralString):
    db = Prisma()
    await db.connect()
    found = await db.recipes.find_many(
        where={
            "name": {
                "contains" : keyword,
                "mode": "insensitive"
            }
        },
        order={
            sorting: 'asc'
        } # type: ignore
        
    )  
    await db.disconnect()
    return found




@app.get("/search/{keyword}/{sorting}/{filtering}")
async def recipesbyKeywordWithSortingAndFiltering(keyword: str, sorting: str, filtering: str, criteria: int):

    db = Prisma()
    await db.connect()
    found = await db.recipes.find_many(
        where={
            "name": {
                "contains" : keyword,
                "mode": "insensitive"
            },
            'OR':  [{filtering.lower():{'gt': criteria}},
                    {filtering.lower(): criteria}]            
        }, # type: ignore
        order={
            sorting: 'asc'
        } # type: ignore
        
    )  
    await db.disconnect()
    return found

    return found_json
@app.get("/healthcheck")
async def healthcheck():
    return "healthy"

@app.get("/recipes", response_model=list[models.RECIPES])
async def recipes():
    found_json = "[]"
    db = Prisma()
    await db.connect()
    found = await db.recipes.find_many()
    await db.disconnect()
    return found

@app.get("/recipes/{recipe_id}", response_model=list[models.RECIPES])#, response_model=models.RECIPES)
async def recipesId(recipe_id: int):
    db = Prisma()
    await db.connect()
    found = await db.recipes.find_many(where={'id': recipe_id})
    await db.disconnect()
    return found
@app.get("/recommend")
async def emptyRecommend():
    message="Please enter a user id after /recommend/"
    return message


@app.get("/recommend/{user_id}")
async def RunRecommend(user_id: int, debug=False, verbose=True):
    recommendedIdsJson = "[]"
    db = Prisma()
    await db.connect()
    userfavs = await db.user_likes_recipes.find_many(
        where={'USER_id': user_id}#,
        # include={
        #     'recipe': True
        # }
    )
    userfavs_ids = [fav.RECIPE_id for fav in userfavs]
    if userfavs_ids.__len__() == 0:
        # raise HTTPException(status_code=204,
        #                     detail="User has no favorites",
        #                     headers={"Content-Error": "User has no favorites"})
        return recommendedIdsJson
    user_db_recipes = await db.recipes.find_many(where={
        'id': {
            'in': userfavs_ids
        }
    })
    all_db_recipes = await db.recipes.find_many()
    print(f'user_db_recipes: {user_db_recipes}') if debug else None
    print(f'all_db_recipes: {all_db_recipes}') if debug else None
    await db.disconnect()
    # convert found : List[RECPIES] to json
    all_db_recipes_json, all_db_recipes_df = list_recipes_to_json_df(all_db_recipes)
    userfavs_json, userfavs_df = list_recipes_to_json_df(user_db_recipes)
    print(all_db_recipes_df) if debug else None
    print(userfavs_df) if debug else None
    #save_both_to_csv(all_db_recipes_df,userfavs_df)
    all_db_recipes_df.to_csv('all_db_recipes.csv') if debug else None
    userfavs_df.to_csv('userfavs.csv') if debug else None
    # recommendedIds=FoodRecommender.recommend(chosenByUser=userfavs_df,restOfDatabase=all_db_recipes_df, debug=True)
    recommendedIds=createRecommendations(userfavs_df,all_db_recipes_df)
    # print(userfavs)
    recommendedIdsJson=recommendedIds.to_json(orient="records")
    print(f'recommended ids:\n {prettifyJson(recommendedIdsJson)}') if verbose else None
    return recommendedIdsJson


# @app.post("/createRecipe", response_model=models.RECIPES)
# async def createRecipe(recipe: RECIPESWithoutId):#(recipejson: str):

#     #TODO: ADD DEBUG TO ARGS after testing with json
#     debug = False
#     print(f'loaded recipe: {json.dumps(recipe, indent=2)}') if debug else None
#     imported_recipe = await import_recipes(recipe, output_id=True, debug=True, verbose=True)
#     print(f'imported recipe: {imported_recipe.json(indent=2)}') if debug else None

#     return imported_recipe

@app.post("/createRecipe", response_model=models.RECIPES)
async def createRecipe(recipe: dict):#(recipejson: str):

    # Create a new recipe
    # recipejson = "{\"name\": \"Homemade Cinnamon Rolls\", \"slug\": \"homemade-cinnamon-rolls\", \"video_url\": \"https://vid.tasty.co/output/25812/mp4_640x640/1488912074\", \"thumbnail_url\": \"https://img.buzzfeed.com/video-api-prod/assets/9d589367531e4c12a4937e30e521c865/fbthumb.jpg\", \"ratings_negative\": 475, \"ratings_positive\": 17340, \"score\": 98, \"cooking_style_big_batch\": 1, \"cooking_style_kid_friendly\": 1, \"cooking_style_bake\": 1, \"meal_breakfast\": 1, \"meal_bakery_goods\": 1, \"cuisine_american\": 1, \"meal_drinks\": 0, \"difficulty_5_ingredients_or_less\": 0, \"healthy_low_calorie\": 0, \"difficulty_easy\": 0, \"dietary_gluten_free\": 0, \"dietary_vegetarian\": 0, \"difficulty_under_1_hour\": 0, \"difficulty_under_45_minutes\": 0, \"healthy_high_protein\": 0, \"dietary_kid_friendly\": 1, \"cuisine_fusion\": 0, \"method_steam\": 0, \"cuisine_japanese\": 0, \"dietary_comfort_food\": 0, \"dietary_indulgent_sweets\": 1, \"method_bake\": 1, \"dietary_dairy_free\": 0, \"cooking_style_one_pot_or_pan\": 0, \"cooking_style_pan_fry\": 0, \"dietary_healthy\": 0, \"method_pan_fry\": 0, \"healthy_low_fat\": 0, \"healthy_low_sugar\": 0, \"healthy_low_carb\": 0, \"cooking_style_mashup\": 0, \"meal_snacks\": 0, \"seasonal_winter\": 0, \"cuisine_british\": 0, \"cooking_style_comfort_food\": 0, \"healthy_high_fiber\": 0, \"cuisine_french\": 0, \"meal_desserts\": 0, \"difficulty_under_15_minutes\": 0, \"difficulty_under_30_minutes\": 0, \"dietary_keto\": 0, \"seasonal_summer\": 0, \"cooking_style_no_bake_desserts\": 0, \"dietary_vegan\": 0, \"cuisine_mexican\": 0, \"seasonal_spring\": 0, \"cuisine_italian\": 0, \"meal_lunch\": 0, \"seasonal_fall\": 0, \"cuisine_german\": 0, \"cooking_style_meal_prep\": 0, \"meal_dinner\": 0, \"meal_appetizers\": 0, \"meal_sides\": 0, \"cuisine_african\": 0, \"cuisine_middle_eastern\": 0, \"method_deep_fry\": 0, \"cuisine_latin_american\": 0, \"method_grill\": 0, \"cuisine_dominican\": 0, \"dietary_pescatarian\": 0, \"cuisine_seafood\": 0, \"cuisine_chinese\": 0, \"cuisine_greek\": 0, \"dietary_contains_alcohol\": 0, \"cuisine_indian\": 0, \"cooking_style_steam\": 0, \"cooking_style_stuffed\": 0, \"cuisine_caribbean\": 0, \"cuisine_filipino\": 0, \"cuisine_taiwanese\": 0, \"cuisine_korean\": 0, \"cuisine_jamaican\": 0, \"meal_brunch\": 0, \"cuisine_swedish\": 0, \"cooking_style_deep_fry\": 0, \"cuisine_west_african\": 0, \"cuisine_thai\": 0, \"cuisine_vietnamese\": 0, \"cuisine_peruvian\": 0, \"cuisine_brazilian\": 0, \"cooking_style_grill\": 0, \"cuisine_bbq\": 0, \"cuisine_kenyan\": 0, \"cuisine_haitian\": 0, \"cuisine_persian\": 0, \"cuisine_ethiopian\": 0, \"cuisine_cuban\": 0, \"cuisine_puerto_rican\": 0, \"cuisine_soul_food\": 0, \"cuisine_indigenous\": 0, \"cuisine_laotian\": 0, \"cuisine_hawaiian\": 0, \"method_no_bake_desserts\": 0, \"cuisine_lebanese\": 0, \"cuisine_south_african\": 0, \"cuisine_venezuelan\": 0}"
    # recipejson = "{\"id\": 1,\"name\": \"Homemade Cinnamon Rolls\", \"slug\": \"homemade-cinnamon-rolls\", \"video_url\": \"https://vid.tasty.co/output/25812/mp4_640x640/1488912074\", \"thumbnail_url\": \"https://img.buzzfeed.com/video-api-prod/assets/9d589367531e4c12a4937e30e521c865/fbthumb.jpg\", \"ratings_negative\": 475, \"ratings_positive\": 17340, \"score\": 98, \"cooking_style_big_batch\": 1, \"cooking_style_kid_friendly\": 1, \"cooking_style_bake\": 1, \"meal_breakfast\": 1, \"meal_bakery_goods\": 1, \"cuisine_american\": 1, \"meal_drinks\": 0, \"difficulty_5_ingredients_or_less\": 0, \"healthy_low_calorie\": 0, \"difficulty_easy\": 0, \"dietary_gluten_free\": 0, \"dietary_vegetarian\": 0, \"difficulty_under_1_hour\": 0, \"difficulty_under_45_minutes\": 0, \"healthy_high_protein\": 0, \"dietary_kid_friendly\": 1, \"cuisine_fusion\": 0, \"method_steam\": 0, \"cuisine_japanese\": 0, \"dietary_comfort_food\": 0, \"dietary_indulgent_sweets\": 1, \"method_bake\": 1, \"dietary_dairy_free\": 0, \"cooking_style_one_pot_or_pan\": 0, \"cooking_style_pan_fry\": 0, \"dietary_healthy\": 0, \"method_pan_fry\": 0, \"healthy_low_fat\": 0, \"healthy_low_sugar\": 0, \"healthy_low_carb\": 0, \"cooking_style_mashup\": 0, \"meal_snacks\": 0, \"seasonal_winter\": 0, \"cuisine_british\": 0, \"cooking_style_comfort_food\": 0, \"healthy_high_fiber\": 0, \"cuisine_french\": 0, \"meal_desserts\": 0, \"difficulty_under_15_minutes\": 0, \"difficulty_under_30_minutes\": 0, \"dietary_keto\": 0, \"seasonal_summer\": 0, \"cooking_style_no_bake_desserts\": 0, \"dietary_vegan\": 0, \"cuisine_mexican\": 0, \"seasonal_spring\": 0, \"cuisine_italian\": 0, \"meal_lunch\": 0, \"seasonal_fall\": 0, \"cuisine_german\": 0, \"cooking_style_meal_prep\": 0, \"meal_dinner\": 0, \"meal_appetizers\": 0, \"meal_sides\": 0, \"cuisine_african\": 0, \"cuisine_middle_eastern\": 0, \"method_deep_fry\": 0, \"cuisine_latin_american\": 0, \"method_grill\": 0, \"cuisine_dominican\": 0, \"dietary_pescatarian\": 0, \"cuisine_seafood\": 0, \"cuisine_chinese\": 0, \"cuisine_greek\": 0, \"dietary_contains_alcohol\": 0, \"cuisine_indian\": 0, \"cooking_style_steam\": 0, \"cooking_style_stuffed\": 0, \"cuisine_caribbean\": 0, \"cuisine_filipino\": 0, \"cuisine_taiwanese\": 0, \"cuisine_korean\": 0, \"cuisine_jamaican\": 0, \"meal_brunch\": 0, \"cuisine_swedish\": 0, \"cooking_style_deep_fry\": 0, \"cuisine_west_african\": 0, \"cuisine_thai\": 0, \"cuisine_vietnamese\": 0, \"cuisine_peruvian\": 0, \"cuisine_brazilian\": 0, \"cooking_style_grill\": 0, \"cuisine_bbq\": 0, \"cuisine_kenyan\": 0, \"cuisine_haitian\": 0, \"cuisine_persian\": 0, \"cuisine_ethiopian\": 0, \"cuisine_cuban\": 0, \"cuisine_puerto_rican\": 0, \"cuisine_soul_food\": 0, \"cuisine_indigenous\": 0, \"cuisine_laotian\": 0, \"cuisine_hawaiian\": 0, \"method_no_bake_desserts\": 0, \"cuisine_lebanese\": 0, \"cuisine_south_african\": 0, \"cuisine_venezuelan\": 0}"
    # recipe_dict = json.loads(recipejson)
    print(f'loaded recipe: {json.dumps(recipe, indent=2)}') if debug else None

    imported_recipe = await import_recipes(recipe, output_id=True, debug=True, verbose=True)
    print(f'imported recipe: {imported_recipe.json(indent=2)}') if debug else None

    return imported_recipe


@app.post("/CreateRecipeFromJson", response_model=models.RECIPES)
async def CreateRecipeFromJson(recipejson: str, debug=False, verbose=True):

    # Create a new recipe
    # recipejson = "{\"name\": \"Homemade Cinnamon Rolls\", \"slug\": \"homemade-cinnamon-rolls\", \"video_url\": \"https://vid.tasty.co/output/25812/mp4_640x640/1488912074\", \"thumbnail_url\": \"https://img.buzzfeed.com/video-api-prod/assets/9d589367531e4c12a4937e30e521c865/fbthumb.jpg\", \"ratings_negative\": 475, \"ratings_positive\": 17340, \"score\": 98, \"cooking_style_big_batch\": 1, \"cooking_style_kid_friendly\": 1, \"cooking_style_bake\": 1, \"meal_breakfast\": 1, \"meal_bakery_goods\": 1, \"cuisine_american\": 1, \"meal_drinks\": 0, \"difficulty_5_ingredients_or_less\": 0, \"healthy_low_calorie\": 0, \"difficulty_easy\": 0, \"dietary_gluten_free\": 0, \"dietary_vegetarian\": 0, \"difficulty_under_1_hour\": 0, \"difficulty_under_45_minutes\": 0, \"healthy_high_protein\": 0, \"dietary_kid_friendly\": 1, \"cuisine_fusion\": 0, \"method_steam\": 0, \"cuisine_japanese\": 0, \"dietary_comfort_food\": 0, \"dietary_indulgent_sweets\": 1, \"method_bake\": 1, \"dietary_dairy_free\": 0, \"cooking_style_one_pot_or_pan\": 0, \"cooking_style_pan_fry\": 0, \"dietary_healthy\": 0, \"method_pan_fry\": 0, \"healthy_low_fat\": 0, \"healthy_low_sugar\": 0, \"healthy_low_carb\": 0, \"cooking_style_mashup\": 0, \"meal_snacks\": 0, \"seasonal_winter\": 0, \"cuisine_british\": 0, \"cooking_style_comfort_food\": 0, \"healthy_high_fiber\": 0, \"cuisine_french\": 0, \"meal_desserts\": 0, \"difficulty_under_15_minutes\": 0, \"difficulty_under_30_minutes\": 0, \"dietary_keto\": 0, \"seasonal_summer\": 0, \"cooking_style_no_bake_desserts\": 0, \"dietary_vegan\": 0, \"cuisine_mexican\": 0, \"seasonal_spring\": 0, \"cuisine_italian\": 0, \"meal_lunch\": 0, \"seasonal_fall\": 0, \"cuisine_german\": 0, \"cooking_style_meal_prep\": 0, \"meal_dinner\": 0, \"meal_appetizers\": 0, \"meal_sides\": 0, \"cuisine_african\": 0, \"cuisine_middle_eastern\": 0, \"method_deep_fry\": 0, \"cuisine_latin_american\": 0, \"method_grill\": 0, \"cuisine_dominican\": 0, \"dietary_pescatarian\": 0, \"cuisine_seafood\": 0, \"cuisine_chinese\": 0, \"cuisine_greek\": 0, \"dietary_contains_alcohol\": 0, \"cuisine_indian\": 0, \"cooking_style_steam\": 0, \"cooking_style_stuffed\": 0, \"cuisine_caribbean\": 0, \"cuisine_filipino\": 0, \"cuisine_taiwanese\": 0, \"cuisine_korean\": 0, \"cuisine_jamaican\": 0, \"meal_brunch\": 0, \"cuisine_swedish\": 0, \"cooking_style_deep_fry\": 0, \"cuisine_west_african\": 0, \"cuisine_thai\": 0, \"cuisine_vietnamese\": 0, \"cuisine_peruvian\": 0, \"cuisine_brazilian\": 0, \"cooking_style_grill\": 0, \"cuisine_bbq\": 0, \"cuisine_kenyan\": 0, \"cuisine_haitian\": 0, \"cuisine_persian\": 0, \"cuisine_ethiopian\": 0, \"cuisine_cuban\": 0, \"cuisine_puerto_rican\": 0, \"cuisine_soul_food\": 0, \"cuisine_indigenous\": 0, \"cuisine_laotian\": 0, \"cuisine_hawaiian\": 0, \"method_no_bake_desserts\": 0, \"cuisine_lebanese\": 0, \"cuisine_south_african\": 0, \"cuisine_venezuelan\": 0}"
    # recipejson = "{\"id\": 1,\"name\": \"Homemade Cinnamon Rolls\", \"slug\": \"homemade-cinnamon-rolls\", \"video_url\": \"https://vid.tasty.co/output/25812/mp4_640x640/1488912074\", \"thumbnail_url\": \"https://img.buzzfeed.com/video-api-prod/assets/9d589367531e4c12a4937e30e521c865/fbthumb.jpg\", \"ratings_negative\": 475, \"ratings_positive\": 17340, \"score\": 98, \"cooking_style_big_batch\": 1, \"cooking_style_kid_friendly\": 1, \"cooking_style_bake\": 1, \"meal_breakfast\": 1, \"meal_bakery_goods\": 1, \"cuisine_american\": 1, \"meal_drinks\": 0, \"difficulty_5_ingredients_or_less\": 0, \"healthy_low_calorie\": 0, \"difficulty_easy\": 0, \"dietary_gluten_free\": 0, \"dietary_vegetarian\": 0, \"difficulty_under_1_hour\": 0, \"difficulty_under_45_minutes\": 0, \"healthy_high_protein\": 0, \"dietary_kid_friendly\": 1, \"cuisine_fusion\": 0, \"method_steam\": 0, \"cuisine_japanese\": 0, \"dietary_comfort_food\": 0, \"dietary_indulgent_sweets\": 1, \"method_bake\": 1, \"dietary_dairy_free\": 0, \"cooking_style_one_pot_or_pan\": 0, \"cooking_style_pan_fry\": 0, \"dietary_healthy\": 0, \"method_pan_fry\": 0, \"healthy_low_fat\": 0, \"healthy_low_sugar\": 0, \"healthy_low_carb\": 0, \"cooking_style_mashup\": 0, \"meal_snacks\": 0, \"seasonal_winter\": 0, \"cuisine_british\": 0, \"cooking_style_comfort_food\": 0, \"healthy_high_fiber\": 0, \"cuisine_french\": 0, \"meal_desserts\": 0, \"difficulty_under_15_minutes\": 0, \"difficulty_under_30_minutes\": 0, \"dietary_keto\": 0, \"seasonal_summer\": 0, \"cooking_style_no_bake_desserts\": 0, \"dietary_vegan\": 0, \"cuisine_mexican\": 0, \"seasonal_spring\": 0, \"cuisine_italian\": 0, \"meal_lunch\": 0, \"seasonal_fall\": 0, \"cuisine_german\": 0, \"cooking_style_meal_prep\": 0, \"meal_dinner\": 0, \"meal_appetizers\": 0, \"meal_sides\": 0, \"cuisine_african\": 0, \"cuisine_middle_eastern\": 0, \"method_deep_fry\": 0, \"cuisine_latin_american\": 0, \"method_grill\": 0, \"cuisine_dominican\": 0, \"dietary_pescatarian\": 0, \"cuisine_seafood\": 0, \"cuisine_chinese\": 0, \"cuisine_greek\": 0, \"dietary_contains_alcohol\": 0, \"cuisine_indian\": 0, \"cooking_style_steam\": 0, \"cooking_style_stuffed\": 0, \"cuisine_caribbean\": 0, \"cuisine_filipino\": 0, \"cuisine_taiwanese\": 0, \"cuisine_korean\": 0, \"cuisine_jamaican\": 0, \"meal_brunch\": 0, \"cuisine_swedish\": 0, \"cooking_style_deep_fry\": 0, \"cuisine_west_african\": 0, \"cuisine_thai\": 0, \"cuisine_vietnamese\": 0, \"cuisine_peruvian\": 0, \"cuisine_brazilian\": 0, \"cooking_style_grill\": 0, \"cuisine_bbq\": 0, \"cuisine_kenyan\": 0, \"cuisine_haitian\": 0, \"cuisine_persian\": 0, \"cuisine_ethiopian\": 0, \"cuisine_cuban\": 0, \"cuisine_puerto_rican\": 0, \"cuisine_soul_food\": 0, \"cuisine_indigenous\": 0, \"cuisine_laotian\": 0, \"cuisine_hawaiian\": 0, \"method_no_bake_desserts\": 0, \"cuisine_lebanese\": 0, \"cuisine_south_african\": 0, \"cuisine_venezuelan\": 0}"
    recipe = json.loads(recipejson)
    print(f'loaded recipe: {json.dumps(recipe, indent=2)}') if debug else None
    imported_recipe = await import_recipes(recipe, output_id=True, debug=True, verbose=True)
    print(f'imported recipe: {imported_recipe.json(indent=2)}') if debug else None

    return imported_recipe

@app.post("/user/{user_id}/like/{recipe_id}", response_model=models.USER_likes_RECIPES)
async def setLikedRecipes(user_id: int, recipe_id: int):
    db = Prisma()
    await db.connect()
    userfavs = await db.user_likes_recipes.create(
    data={
        "USER_id": user_id,
        "RECIPE_id": recipe_id
    }
    )
    await db.disconnect()
    return userfavs

@app.post("/user/{user_id}/owns/{recipe_id}", response_model=models.USER_owns_RECIPES)
async def setOwnedRecipes(user_id: int, recipe_id: int):
    db = Prisma()
    await db.connect()
    userowns = await db.user_owns_recipes.create(
    data={
        "USER_id": user_id,
        "RECIPE_id": recipe_id
    }
    )
    await db.disconnect()
    return userowns

@app.get("/liked-recipes/{user_id}")
async def getLikedRecipes(user_id: int):
    db = Prisma()
    await db.connect()
    userfavs = await db.user_likes_recipes.find_many(
        where={'USER_id': user_id}
    )
    userfavs_ids = [fav.RECIPE_id for fav in userfavs]
    user_db_recipes = await db.recipes.find_many(where={
        'id': {
            'in': userfavs_ids
        }
    })
    await db.disconnect()
    return user_db_recipes

@app.get("/owned-recipes/{user_id}")
async def getOwnedRecipes(user_id: int):
    db = Prisma()
    await db.connect()
    user_db_recipes = await db.user_owns_recipes.find_many( #userowns
        where={'USER_id': user_id},
        include={
            'recipe': True
        }
    )
    # userowns_ids = [owns.RECIPE_id for owns in userowns]
    # user_db_recipes = await db.recipes.find_many(where={
    #     'id': {
    #         'in': userowns_ids
    #     }
    # })
    await db.disconnect()
    return user_db_recipes

@app.get("/delete/user/{user_id}/like/{recipe_id}")
async def deleteLikedRecipes(user_id: int, recipe_id: int):
    db = Prisma()
    await db.connect()
    userfavs = await db.user_likes_recipes.delete(
        where={
            "USER_id_RECIPE_id": {"RECIPE_id": recipe_id, "USER_id": user_id}
        }
    )
    await db.disconnect()
    return userfavs

@app.get("/delete/user/{user_id}/owns/{recipe_id}")
async def deleteOwnedRecipes(user_id: int, recipe_id: int):
    db = Prisma()
    await db.connect()
    userowns = await db.user_owns_recipes.delete(
        where={
            "USER_id_RECIPE_id": {"RECIPE_id": recipe_id, "USER_id": user_id}
        }
    )
    await db.disconnect()
    return userowns
@app.get("/ingredients/{recipe_id}", response_model=list[models.INGREDIENTS] | str)
async def getIngredients(recipe_id: int, debug=False, verbose=True): 
    db = Prisma()
    await db.connect()
    ingredients = await db.ingredients.find_many(
        where={ "recipe_id": recipe_id}
    )
    if len(ingredients) > 0 :
        print(f'ingredients found in db: {ingredients}') if verbose else None
        return ingredients
    else:
        responding_recipe = await db.recipes.find_first(where={'id': recipe_id})
        print(f'recipe found in db: {responding_recipe}') if debug else None
        if responding_recipe is not None:
            slug = responding_recipe.slug
        else:
            return "recipe not found"
        print(f'slug: {slug}') if debug else None
        filename="ingredients.csv"
        dataset_abs_path = (mod_path / filename).resolve()
        df = pd.read_csv(fr'{dataset_abs_path}')
        df = df[df['recipe_id'] == slug]
        print(f'df: {df}') if debug else None
        rows = df.itertuples(index=False)
        new_ingredients : list[models.INGREDIENTS] = [] 
        ingredient = {}
        for row in rows:
            ingredient = row._asdict() 
            print(f'ingredient: {ingredient}') if debug else None
            new_ingredients.append(await import_ingredient(ingredient, output_id=True, debug=False, verbose=False))
        print(f'new_ingredients: {new_ingredients}') if verbose else None
    await db.disconnect()
    return new_ingredients

@app.get("/instructions/{recipe_id}", response_model=list[models.INSTRUCTIONS] | str)
async def getIntructions(recipe_id: int, debug=False, verbose=True): 
    db = Prisma()
    await db.connect()
    instructions = await db.instructions.find_many(
        where={ "recipe_id": recipe_id}
    )
    if len(instructions) > 0 :
        print(f'instructions found in db: {instructions}') if verbose else None
        return instructions
    else:
        responding_recipe = await db.recipes.find_first(where={'id': recipe_id})
        print(f'recipe found in db: {responding_recipe}') if debug else None
        if responding_recipe is not None:
            slug = responding_recipe.slug
        else:
            return "recipe not found"
        print(f'slug: {slug}') if debug else None
        filename="instructions.csv"
        dataset_abs_path = (mod_path / filename).resolve()
        df = pd.read_csv(fr'{dataset_abs_path}')
        df = df[df['recipe_id'] == slug]
        print(f'df: {df}') if debug else None
        rows = df.itertuples(index=False)
        new_instructions : list[models.INSTRUCTIONS] = [] 
        instruction = {}
        for row in rows:
            instruction = row._asdict() 
            print(f'instruction: {instruction}') if debug else None
            new_instructions.append(await import_instruction(instruction, output_id=True, debug=False, verbose=False))
        print(f'new_instructions: {new_instructions}') if verbose else None
    await db.disconnect()
    return new_instructions
@app.post("/upsert/ingredients/", response_model=models.INGREDIENTS)
async def upsertIngredients(ingredient: types.INGREDIENTSCreateInput)-> models.INGREDIENTS :
    # db = Prisma()
    # await db.connect()
    # new_ingredient = await db.ingredients.create(
    #     data=ingredient
    # )
    # await db.disconnect()
    new_ingredient = await import_ingredient(ingredient, output_id=True, debug=False, verbose=False) # type: ignore
    return new_ingredient

@app.post("/upsert/instructions/", response_model=models.INSTRUCTIONS)
async def upsertInstructions(instruction: types.INSTRUCTIONSCreateInput)-> models.INSTRUCTIONS :
    # db = Prisma()
    # await db.connect()
    # new_instruction = await db.instructions.create(
    #     data=instruction
    # )
    # await db.disconnect()
    new_instruction = await import_instruction(instruction, output_id=True, debug=False, verbose=False) # type: ignore
    return new_instruction
@app.get("/delete/ingredients/{ingredient_id}", response_model=models.INGREDIENTS)
async def deleteIngredients(ingredient_id: int ):
    db = Prisma()
    await db.connect()
    ingredients = await db.ingredients.delete(
        where={
            "id": ingredient_id,
        }
    )
    await db.disconnect()
    return ingredients

@app.get("/delete/instructions/{instruction_id}", response_model=models.INSTRUCTIONS)
async def deleteInstructions(instruction_id: int ):
    db = Prisma()
    await db.connect()
    instructions = await db.instructions.delete(
        where={
            "id": instruction_id,
        }
    )
    await db.disconnect()
    return instructions


@app.post("/create/user/", response_model=models.USERS)
async def createUser(user: types.USERSCreateInput )-> models.USERS :
    db = Prisma()
    await db.connect()
    new_user = await db.users.create(
        data=user
    )
    await db.disconnect()
    return new_user
@app.get("/delete/user/{user_id}", response_model=models.USERS)
async def deleteUser(user_id: int):
    db = Prisma()
    await db.connect()
    user = await db.users.delete(
        where={'id': user_id}
    )
    await db.disconnect()
    return user

@app.get("/users/", response_model=list[models.USERS])
async def getUsers():
    db = Prisma()
    await db.connect()
    users = await db.users.find_many()
    await db.disconnect()
    return users

@app.post("/update/user/", response_model=models.USERS)
async def updateUser(user: types.USERSUpdateInput):
    db = Prisma()
    await db.connect()
    updated_user = await db.users.update(
    where={
        'id': user["id"], # type: ignore
    },
    data=user,
    )
    await db.disconnect()
    return updated_user

@app.get("/users/{user_id}", response_model=models.USERS)
async def getUser(user_id: int):
    db = Prisma()
    await db.connect()
    user = await db.users.find_first(where={'id': user_id})
    await db.disconnect()
    return user

@app.get("/usersbyname/{user_name}", response_model=models.USERS)
async def getUserbyname(user_name: str):
    db = Prisma()
    await db.connect()
    user = await db.users.find_first(where={'name': user_name})
    await db.disconnect()
    return user


@app.get("/isLiked/{user_id}/{recipe_id}", response_model=bool)
async def isLiked(user_id: int, recipe_id: int):
    db = Prisma()
    await db.connect()
    userfavs = await db.user_likes_recipes.find_first(
        where={'USER_id': user_id, 'RECIPE_id': recipe_id}
    )
    await db.disconnect()
    if userfavs is None:
        return False
    return True




#python3 main.py
async def main() -> None:
    db = Prisma()
    await db.connect()

    # Create a new recipe
    recipe = await db.recipes.create({
        'id': 1,
        'name': "Cinnamon Roll Coffee Cake",
        'slug': "cinnamon-roll-coffee-cake",
        'thumbnail_url': "https://img.buzzfeed.com/thumbnailer-prod-us-east-1/video-api/assets/449848.jpg?resize=600:*&output-format=auto&output-quality=auto",
    })
    print(f'created recipe: {recipe.json(indent=2)}')

    found = await db.recipes.find_many(where={'id': recipe.id})
    assert found is not None
    for recipe in found:
        print(f'found recipe: {recipe.json(indent=2)}')
    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())