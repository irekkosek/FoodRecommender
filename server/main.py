import asyncio
from os import name
import re
from numpy import rec, where
from prisma import Prisma
from fastapi import FastAPI
import json

app = FastAPI()

#uvicorn main:app --reload
@app.get("/")
async def root():
    db = Prisma()
    await db.connect()
    found = await db.recipes.find_many(where={
        'OR' : [
            {'id': 1},
            {'id': 27}
            ]
        }
    )
    await db.disconnect()

    # convert found : List[RECPIES] to json
    found_json = []
    for recipe in found:
        found_json.append(recipe.json())
    
    return found_json


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



