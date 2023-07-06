import asyncio
from doctest import debug
from os import name
import re
from numpy import rec, where
from prisma import Prisma, types, models
from fastapi import FastAPI
import json
import pandas as pd
from FoodRecommender import FoodRecommender
from FoodRecommender import createRecommendations
from import_recipes import import_recipes
from prisma.partials import RECIPESWithoutId
from fastapi.middleware.cors import CORSMiddleware

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
    db = Prisma()
    await db.connect()
    userfavs = await db.user_likes_recipes.find_many(
        where={'USER_id': user_id}#,
        # include={
        #     'recipe': True
        # }
    )
    userfavs_ids = [fav.RECIPE_id for fav in userfavs]
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


@app.post("/createRecipe", response_model=models.RECIPES)
async def createRecipe(recipe: RECIPESWithoutId):#(recipejson: str):

    #TODO: ADD DEBUG TO ARGS after testing with json
    debug = False
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



