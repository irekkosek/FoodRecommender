import asyncio
from os import name
import re
from numpy import rec, where, reciprocal
from prisma import Prisma
from fastapi import FastAPI
import json
import pandas as pd
from pydantic import BaseModel

app = FastAPI()
db = Prisma()
bool = False
#uvicorn main:app --reload
# @app.get("/read/{id}")
# async def root():
#     db = Prisma()
#     await db.connect()
#     found = await db.recipes.find_many(where={
#         'OR' : [
#             {'id': 1},
#             {'id': 27}
#             ]
#         }
#     )

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


@app.get("/recipes")
async def recipes():
    db = Prisma()
    await db.connect()
    found = await db.recipes.find_many()
    await db.disconnect()

    # convert found : List[RECPIES] to json
    found_json = []
    found_json, df = list_recipes_to_json_df(found)
    print(df.head())

    return found_json

@app.post("user/create")
async def usercreate(user: User):
    db=Prisma()
    await db.connect()
    user=await db.users.create(
        {'name': user.name,
        'password': user.password
    })

@app.get("/recipes/{slug}")
async def recipesId(slug: str):
    db = Prisma()
    await db.connect()
    found = await db.recipes.find_many(where={'slug': slug})
    await db.disconnect()

    # convert found : List[RECPIES] to json
    # found_json = []
    found_json, df = list_recipes_to_json_df(found)
    print(df.head())
    
    return found_json

def list_recipes_to_json_df(found):
    found_json = "["
    for recipe in found:
        # found.__dict__
        found_json += f'{recipe.json()},'
    found_json = found_json[:-1] + "]"
    df = pd.read_json(found_json)
    return found_json,df


# @app.delete("/delete")
# async def delete(db):

#     recipe= await db.recipes.delete(where={'id':1})


# @app.delete("/delete/{slug}")
# async def delete(slug: str):
#     db = Prisma()
#     await db.connect()
#     recipe= await db.recipes.delete(where={'slug':slug})
#     await db.disconnect()


@app.post("/recipes/create")
async def create(recipe: Recipe):
    db = Prisma()
    await db.connect()
    recipe = await db.recipes.create(
       {
           'name': recipe.name,
           'slug': recipe.slug,
           'thumbnail_url': recipe.thumbnail_url
       }
        
    
    )
    await db.disconnect()


# @app.get("/create/recipes")
# async def create():
#     db = Prisma()
#     await db.connect()
#     try:
#         recipe = await db.recipes.create(
#                 data={
#             'id': 1,
#             'name': "Cinnamon Roll Coffee Cake",
#             'slug': "cinnamon-roll-coffee-cake",
#             'thumbnail_url': "https://img.buzzfeed.com/thumbnailer-prod-us-east-1/video-api/assets/449848.jpg?resize=600:*&output-format=auto&output-quality=auto",
#             }
        
    
#     )
        
#     except Exception as e:  
#         return{"error ":str(e)}
    

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


app.get("/search/{keyword}")
async def recipes(keyword: str):
    db = Prisma()
    await db.connect()
    all_recipes = await db.recipes.find_many()  # Pobierz wszystkie przepisy z bazy danych
    await db.disconnect()

    # Filtruj przepisy, aby zwrócić tylko te, których id zawiera keyword
    found = [recipe for recipe in all_recipes if str(keyword) in str(recipe.name)]

    # Konwertuj found : List[RECIPES] na JSON
    found_json, df = list_recipes_to_json_df(found)
    print(df.head())

    return found_json


@app.post("/recipes/delete/{recipe_id}")
async def delete(recipe_id: int, recipe: Recipe):
    db = Prisma()
    await db.connect()
    recipe =await db.recipes.delete(
        where={'id': recipe_id}
    )
    await db.disconnect()

@app.get("/search/{keyword}/{sorting}")
async def recipes(keyword: str, sorting: str):
    db = Prisma()
    await db.connect()
    all_recipes = await db.recipes.find_many(order={sorting: 'desc'})  # Pobierz wszystkie przepisy z bazy danych
    await db.disconnect()

    # Filtruj przepisy, aby zwrócić tylko te, których id zawiera keyword
    found = [recipe for recipe in all_recipes if str(keyword) in str(recipe.name)]

    # Konwertuj found : List[RECIPES] na JSON
    found_json, df = list_recipes_to_json_df(found)
    print(df.head())

    return found_json



@app.get("/search/{keyword}/{sorting}/{filtering}")
async def recipes(keyword: str, sorting: str, filtering: str, criteria: int):
    db = Prisma()
    await db.connect()
    all_recipes = await db.recipes.find_many(order={sorting: 'desc'},where={filtering:{'gt': criteria}})  
    await db.disconnect()

    
    found = [recipe for recipe in all_recipes if str(keyword) in str(recipe.name)]

    found_json, df = list_recipes_to_json_df(found)
    print(df.head())

    return found_json




#python3 main.py
async def main() -> None:
    db = Prisma()
    await db.connect()

    # Create a new recipe
    #await create()
    # recipe = await db.recipes.create(
    #    {
    #     'id': 1,
    #     'name': "Cinnamon Roll Coffee Cake",
    #     'slug': "cinnamon-roll-coffee-cake",
    #     'thumbnail_url': "https://img.buzzfeed.com/thumbnailer-prod-us-east-1/video-api/assets/449848.jpg?resize=600:*&output-format=auto&output-quality=auto",
    #     }
        
    
    # )
    # print(f'created recipe: {recipe.json(indent=2)}')

    # Read a recipe
    #recipe = await db.recipes.find_first(where={'id': 1})


    #Update a recipe  
    #await update(db)
   

    # recipe= await db.recipes.update(
    # where={
    #     'id': 1,
    # },
    # data={
    #     'name': "New Cinnamon Roll Coffee Cake", 
    #     'slug': "new-cinammon-roll-coffee-cake",
    #     'thumbnail_url': "https://img.buzzfeed.com/thumbnailer-prod-us-east-1/video-api/assets/449848.jpg?resize=600:*&output-format=auto&output-quality=auto"
    # },
    # )
    # print(f'updated recipe: {recipe.json(indent=2)}')
    
    # Delete a recipe
    #recipe= await db.recipes.delete(where={'id':1})
    #await delete(db)

    # found = await db.recipes.find_many(where={'id': recipe.id})
    # assert found is not None
    # for recipe in found:
    #     print(f'found recipe: {recipe.json(indent=2)}')
    await db.disconnect()









if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())




