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
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    name: str
    password: str



class Recipe(BaseModel):
            name: str
            slug: str
            thumbnail_url: str
            cooking_style_big_batch: int
            cooking_style_kid_friendly: int
            cooking_style_bake: int
            meal_breakfast: int
            meal_bakery_goods: int
            cuisine_american: int
            meal_drinks: int
            difficulty_5_ingredients_or_less: int
            healthy_low_calorie: int
            difficulty_easy: int
            dietary_gluten_free: int
            dietary_vegetarian: int
            difficulty_under_1_hour: int
            difficulty_under_45_minutes: int
            healthy_high_protein: int
            dietary_kid_friendly: int
            cuisine_fusion: int
            method_steam: int
            cuisine_japanese: int
            dietary_comfort_food: int
            dietary_indulgent_sweets: int
            method_bake: int
            dietary_dairy_free: int
            cooking_style_one_pot_or_pan: int
            cooking_style_pan_fry: int
            dietary_healthy: int
            method_pan_fry: int
            healthy_low_fat: int
            healthy_low_sugar: int
            healthy_low_carb: int
            cooking_style_mashup: int
            meal_snacks: int
            seasonal_winter: int
            cuisine_british: int
            cooking_style_comfort_food: int
            healthy_high_fiber: int
            cuisine_french: int
            meal_desserts: int
            difficulty_under_15_minutes: int
            difficulty_under_30_minutes: int
            dietary_keto: int
            seasonal_summer: int
            cooking_style_no_bake_desserts: int
            dietary_vegan: int
            cuisine_mexican: int
            seasonal_spring: int
            cuisine_italian: int
            meal_lunch: int
            seasonal_fall: int
            cuisine_german: int
            cooking_style_meal_prep: int
            meal_dinner: int
            meal_appetizers: int
            meal_sides: int
            cuisine_african: int
            cuisine_middle_eastern: int
            method_deep_fry: int
            cuisine_latin_american: int
            method_grill: int
            cuisine_dominican: int
            dietary_pescatarian: int
            cuisine_seafood: int
            cuisine_chinese: int
            cuisine_greek: int
            dietary_contains_alcohol: int
            cuisine_indian: int
            cooking_style_steam: int
            cooking_style_stuffed: int
            cuisine_caribbean: int
            cuisine_filipino: int
            cuisine_taiwanese: int
            cuisine_korean: int
            cuisine_jamaican: int
            meal_brunch: int
            cuisine_swedish: int
            cooking_style_deep_fry: int
            cuisine_west_african: int
            cuisine_thai: int
            cuisine_vietnamese: int
            cuisine_peruvian: int
            cuisine_brazilian: int
            cooking_style_grill: int
            cuisine_bbq: int
            cuisine_kenyan: int
            cuisine_haitian: int
            cuisine_persian: int
            cuisine_ethiopian: int
            cuisine_cuban: int
            cuisine_puerto_rican: int
            cuisine_soul_food: int
            cuisine_indigenous: int
            cuisine_laotian: int
            cuisine_hawaiian: int
            method_no_bake_desserts: int
            cuisine_lebanese: int
            cuisine_south_african: int
            cuisine_venezuelan: int


@app.post("/recipes/update/{id}")
async def update(recipe: Recipe, id: int):
    db = Prisma()
    await db.connect()
    recipe= await db.recipes.update(
    where={
        'id':id,
    },
    data={
        
            'name': recipe.name,
            'slug': recipe.slug,
            'thumbnail_url': recipe.thumbnail_url,
            'cooking_style_big_batch': recipe.cooking_style_big_batch,
            'cooking_style_kid_friendly': recipe.cooking_style_kid_friendly,
            'cooking_style_bake': recipe.cooking_style_bake,
            'meal_breakfast': recipe.meal_breakfast,
            'meal_bakery_goods': recipe.meal_bakery_goods,
            'cuisine_american': recipe.cuisine_american,
            'meal_drinks': recipe.meal_drinks,
            'difficulty_5_ingredients_or_less': recipe.difficulty_5_ingredients_or_less,
            'healthy_low_calorie': recipe.healthy_low_calorie,
            'difficulty_easy': recipe.difficulty_easy,
            'dietary_gluten_free': recipe.dietary_gluten_free,
            'dietary_vegetarian': recipe.dietary_vegetarian,
            'difficulty_under_1_hour': recipe.difficulty_under_1_hour,
            'difficulty_under_45_minutes': recipe.difficulty_under_45_minutes,
            'healthy_high_protein': recipe.healthy_high_protein,
            'dietary_kid_friendly': recipe.dietary_kid_friendly,
            'cuisine_fusion': recipe.cuisine_fusion,
            'method_steam': recipe.method_steam,
            'cuisine_japanese': recipe.cuisine_japanese,
            'dietary_comfort_food': recipe.dietary_comfort_food,
            'dietary_indulgent_sweets': recipe.dietary_indulgent_sweets,
            'method_bake': recipe.method_bake,
            'dietary_dairy_free': recipe.dietary_dairy_free,
            'cooking_style_one_pot_or_pan': recipe.cooking_style_one_pot_or_pan,
            'cooking_style_pan_fry': recipe.cooking_style_pan_fry,
            'dietary_healthy': recipe.dietary_healthy,
            'method_pan_fry': recipe.method_pan_fry,
            'healthy_low_fat': recipe.healthy_low_fat,
            'healthy_low_sugar': recipe.healthy_low_sugar,
            'healthy_low_carb': recipe.healthy_low_carb,
            'cooking_style_mashup': recipe.cooking_style_mashup,
            'meal_snacks': recipe.meal_snacks,
            'seasonal_winter': recipe.seasonal_winter,
            'cuisine_british': recipe.cuisine_british,
            'cooking_style_comfort_food': recipe.cooking_style_comfort_food,
            'healthy_high_fiber': recipe.healthy_high_fiber,
            'cuisine_french': recipe.cuisine_french,
            'meal_desserts': recipe.meal_desserts,
            'difficulty_under_15_minutes': recipe.difficulty_under_15_minutes,
            'difficulty_under_30_minutes': recipe.difficulty_under_30_minutes,
            'dietary_keto': recipe.dietary_keto,
            'seasonal_summer': recipe.seasonal_summer,
            'cooking_style_no_bake_desserts': recipe.cooking_style_no_bake_desserts,
            'dietary_vegan': recipe.dietary_vegan,
            'cuisine_mexican': recipe.cuisine_mexican,
            'seasonal_spring': recipe.seasonal_spring,
            'cuisine_italian': recipe.cuisine_italian,
            'meal_lunch': recipe.meal_lunch,
            'seasonal_fall': recipe.seasonal_fall,
            'cuisine_german': recipe.cuisine_german,
            'cooking_style_meal_prep': recipe.cooking_style_meal_prep,
            'meal_dinner': recipe.meal_dinner,
            'meal_appetizers': recipe.meal_appetizers,
            'meal_sides': recipe.meal_sides,
            'cuisine_african': recipe.cuisine_african,
            'cuisine_middle_eastern': recipe.cuisine_middle_eastern,
            'method_deep_fry': recipe.method_deep_fry,
            'cuisine_latin_american': recipe.cuisine_latin_american,
            'method_grill': recipe.method_grill,
            'cuisine_dominican': recipe.cuisine_dominican,
            'dietary_pescatarian': recipe.dietary_pescatarian,
            'cuisine_seafood': recipe.cuisine_seafood,
            'cuisine_chinese': recipe.cuisine_chinese,
            'cuisine_greek': recipe.cuisine_greek,
            'dietary_contains_alcohol': recipe.dietary_contains_alcohol,
            'cuisine_indian': recipe.cuisine_indian,
            'cooking_style_steam': recipe.cooking_style_steam,
            'cooking_style_stuffed': recipe.cooking_style_stuffed,
            'cuisine_caribbean': recipe.cuisine_caribbean,
            'cuisine_filipino': recipe.cuisine_filipino,
            'cuisine_taiwanese': recipe.cuisine_taiwanese,
            'cuisine_korean': recipe.cuisine_korean,
            'cuisine_jamaican': recipe.cuisine_jamaican,
            'meal_brunch': recipe.meal_brunch,
            'cuisine_swedish': recipe.cuisine_swedish,
            'cooking_style_deep_fry': recipe.cooking_style_deep_fry,
            'cuisine_west_african': recipe.cuisine_west_african,
            'cuisine_thai': recipe.cuisine_thai,
            'cuisine_vietnamese': recipe.cuisine_vietnamese,
            'cuisine_peruvian': recipe.cuisine_peruvian,
            'cuisine_brazilian': recipe.cuisine_brazilian,
            'cooking_style_grill': recipe.cooking_style_grill,
            'cuisine_bbq': recipe.cuisine_bbq,
            'cuisine_kenyan': recipe.cuisine_kenyan,
            'cuisine_haitian': recipe.cuisine_haitian,
            'cuisine_persian': recipe.cuisine_persian,
            'cuisine_ethiopian': recipe.cuisine_ethiopian,
            'cuisine_cuban': recipe.cuisine_cuban,
            'cuisine_puerto_rican': recipe.cuisine_puerto_rican,
            'cuisine_soul_food': recipe.cuisine_soul_food,
            'cuisine_indigenous': recipe.cuisine_indigenous,
            'cuisine_laotian': recipe.cuisine_laotian,
            'cuisine_hawaiian': recipe.cuisine_hawaiian,
            'method_no_bake_desserts': recipe.method_no_bake_desserts,
            'cuisine_lebanese': recipe.cuisine_lebanese,
            'cuisine_south_african': recipe.cuisine_south_african,
            'cuisine_venezuelan': recipe.cuisine_venezuelan
    },
    )
    await db.disconnect()
    return recipe

@app.post("/recipes/delete/{recipe_id}")
async def delete(recipe_id: int):
    db = Prisma()
    await db.connect()
    recipe =await db.recipes.delete(
        where={'id': recipe_id}
    )
    await db.disconnect()

def list_recipes_to_json_df(found):
    found_json = "["
    for recipe in found:
        # found.__dict__
        found_json += f'{recipe.json()},'
    found_json = found_json[:-1] + "]"
    df = pd.read_json(found_json)
    return found_json,df


@app.post("create/user")
async def create(user: User):
    db=Prisma()
    await db.connect()
    user = await db.users.create({
        'name': user.name,
        'password': user.password
    }
    )

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

@app.get("/search/{keyword}")
async def recipes(keyword: str):
    db = Prisma()
    await db.connect()
    all_recipes = await db.recipes.find_many()  # Pobierz wszystkie przepisy z bazy danych
    await db.disconnect()

    # Filtruj przepisy, aby zwrócić tylko te, których id zawiera keyword
    found = [recipe for recipe in all_recipes if str(keyword.lower()) in str(recipe.name.lower())]

    # Konwertuj found : List[RECIPES] na JSON
    found_json, df = list_recipes_to_json_df(found)
    print(df.head())

    return found_json


@app.get("/search/{keyword}/{sorting}")
async def recipes(keyword: str, sorting: str):
    db = Prisma()
    await db.connect()
    all_recipes = await db.recipes.find_many(order={sorting.lower(): 'desc'})  # Pobierz wszystkie przepisy z bazy danych
    await db.disconnect()

    # Filtruj przepisy, aby zwrócić tylko te, których id zawiera keyword
    found = [recipe for recipe in all_recipes if str(keyword.lower()) in str(recipe.name.lower())]

    # Konwertuj found : List[RECIPES] na JSON
    found_json, df = list_recipes_to_json_df(found)
    print(df.head())

    return found_json



@app.get("/search/{keyword}/{sorting}/{filtering}")
async def recipes(keyword: str, sorting: str, filtering: str, criteria: int):
    db = Prisma()
    await db.connect()
    all_recipes = await db.recipes.find_many(order={sorting.lower(): 'desc'},where={filtering.lower():{'gt': criteria}})  
    await db.disconnect()

    
    found = [recipe for recipe in all_recipes if str(keyword.lower()) in str(recipe.name.lower())]

    found_json, df = list_recipes_to_json_df(found)
    print(df.head())

    return found_json


@app.get("/search/{keyword}/{sorting}/{filtering}")
async def recipes(keyword: str, sorting: str, filtering: str, criteria: int):
    db = Prisma()
    await db.connect()
    all_recipes = await db.recipes.find_many(order={sorting.lower(): 'desc'},where={ 'OR':  [{filtering.lower():{'gt': criteria}}, {filtering.lower(): criteria}  ]})  
    await db.disconnect()
    found = [recipe for recipe in all_recipes if str(keyword.lower()) in str(recipe.name.lower())]

    found_json, df = list_recipes_to_json_df(found)
    print(df.head())

    return found_json


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