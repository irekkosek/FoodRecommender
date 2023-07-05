import asyncio
from doctest import debug
from os import name
from pyexpat import model
import re
from turtle import mode
from numpy import rec
from prisma import Prisma, types, bases, client, builder, models
import pandas as pd
from pathlib import Path
import sys
from prisma.partials import RECIPESWithoutId
import json

args = sys.argv

async def import_recipes(recipe: dict | RECIPESWithoutId , verbose:bool=False, debug:bool=False, output_id:bool=False) -> models.RECIPES:
    db = Prisma()
    await db.connect()
    if type(recipe) is dict:
        # check if video_url is NaN
        if type(recipe['video_url']) is float:
            recipe['video_url'] = None
        # Create a new recipe
        new_recipe_input = types.RECIPESCreateInput(**recipe)
    
    elif type(recipe) is RECIPESWithoutId:
        new_recipe_input = types.RECIPESCreateInput(**json.loads(recipe.json()))
    else:
        raise TypeError("recipe must be a dict or RECIPESWithoutId")
    new_recipe = await db.recipes.create( data=new_recipe_input)

    if verbose:
        print(f'created recipe: {new_recipe.json(indent=2)}')

    if debug:
        found = await db.recipes.find_many(where={'id': new_recipe.id})
        assert found is not None
        for found_recipe in found:
            print(f'found recipe: {found_recipe.json(indent=2)}')
    if output_id:
        print(f'{new_recipe.id}')
    await db.disconnect()
    return new_recipe

if __name__ == '__main__':
    filename="dishes_tags_reworked.csv"
    mod_path = Path(__file__).parent
    dataset_abs_path = (mod_path / filename).resolve()
    df = pd.read_csv(fr'{dataset_abs_path}')

    rows = df.itertuples() #(index=False)
    recipe = {}
    debug = False
    if 'debug' in args or '--debug' in args:
        debug = True
    short = False
    counter = 0
    if 'short' in args or '--short' in args:
        short = True

    for row in rows:
        # change row into dict
        recipe = row._asdict() 
        if short:
            counter+=1
            if counter > 100:
                break
        asyncio.run(import_recipes(recipe, output_id=True))
    
    print("imported recipes complete")
    



