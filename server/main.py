import asyncio
from doctest import debug
from os import name
import re
from numpy import rec, where
from prisma import Prisma
from fastapi import FastAPI
import json
import pandas as pd
from FoodRecommender import FoodRecommender
from FoodRecommender import createRecommendations

app = FastAPI()

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

@app.get("/recipes")
async def recipes():
    db = Prisma()
    await db.connect()
    found = await db.recipes.find_many()
    await db.disconnect()

    # convert found : List[RECPIES] to json
    found_json, df = list_recipes_to_json_df(found)
    print(df.head())
    
    return found_json

@app.get("/recipes/{recipe_id}")
async def recipesId(recipe_id: int):
    db = Prisma()
    await db.connect()
    found = await db.recipes.find_many(where={'id': recipe_id})
    await db.disconnect()

    # convert found : List[RECPIES] to json
    # found_json = []
    found_json, df = list_recipes_to_json_df(found)
    print(df.head())
    
    return found_json
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
    return all_db_recipes_json


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



