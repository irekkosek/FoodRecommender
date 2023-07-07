import asyncio
from turtle import up
from click import progressbar
#from doctest import debug
#from os import name
#from pyexpat import model
#import re
# from turtle import mode
#from numpy import rec
from prisma import Prisma, types, bases, client, builder, models
import pandas as pd
from pathlib import Path
import sys
from prisma.partials import RECIPESWithoutId
import json


args = sys.argv

async def import_recipes(recipe: dict | RECIPESWithoutId ,
    verbose:bool=False, debug:bool=False, output_id:bool=False, progress:bool=False,
    progressbar: str = "") -> models.RECIPES:
    db = Prisma()
    await db.connect()
    if type(recipe) is dict:
        # check if video_url is NaN
        if type(recipe['video_url']) is float:
            recipe['video_url'] = None
        # Create a new recipe
        
        new_recipe_input = types.RECIPESCreateInput(**recipe)
        upsert_recipe_input = types.RECIPESUpsertInput(
            create=types.RECIPESCreateInput(**recipe),update=types.RECIPESUpdateInput(**recipe))
        print(f' upsert_recipe_input : {upsert_recipe_input}')
        new_recipe = await db.recipes.upsert(
        where={'id': recipe['id']},
        data=upsert_recipe_input
    )
    elif type(recipe) is RECIPESWithoutId:
        new_recipe_input = types.RECIPESCreateInput(**json.loads(recipe.json()))
        new_recipe = await db.recipes.create( data=new_recipe_input)

    else:
        raise TypeError("recipe must be a dict or RECIPESWithoutId")


    if verbose:
        print(f'created recipe: {new_recipe.json(indent=2)}')

    if debug:
        found = await db.recipes.find_many(where={'id': new_recipe.id})
        assert found is not None
        for found_recipe in found:
            print(f'found recipe: {found_recipe.json(indent=2)}')
    if output_id:
        if (progress):
            print(f'{progressbar} {new_recipe.id}')
        else:
            print(f'{new_recipe.id}')
    await db.disconnect()
    return new_recipe

if __name__ == '__main__':
    filename="dishes_tags_reworked.csv"
    mod_path = Path(__file__).parent
    dataset_abs_path = (mod_path / filename).resolve()
    df = pd.read_csv(fr'{dataset_abs_path}')

    df_len = len(df.index)
    rows = df.itertuples(index=False)
    recipe = {}
    debug = False
    if 'debug' in args or '--debug' in args:
        debug = True
    short = False
    counter = 1
    if 'short' in args or '--short' in args:
        short = True
        df_len = 100

    for row in rows:
        # change row into dict
        recipe = row._asdict() 
        if short:
            if counter > 100:
                break
        asyncio.run(import_recipes(recipe, output_id=True, progress=True, progressbar=str(f'{counter}/{df_len}:')))
        counter+=1

    print("imported recipes complete")
    



