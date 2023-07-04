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



class Recipe(BaseModel):
    name: str
    slug: str
    thumbnail_url: str


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
           'thumbnail_url': recipe.thumbnail_url
    },
    )
    await db.disconnect()


@app.post("/recipes/delete/{recipe_id}")
async def delete(recipe_id: int, recipe: Recipe):
    db = Prisma()
    await db.connect()
    recipe =await db.recipes.delete(
        where={'id': recipe_id}
    )
    await db.disconnect()



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




