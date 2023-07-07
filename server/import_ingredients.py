from calendar import c
from pathlib import Path
import select
from unittest import skip
from numpy import NaN
import pandas as pd
import sys
import asyncio
args = sys.argv
from prisma import Prisma, types, bases, client, builder, models, errors
import json


async def import_ingredient(ingredient: dict  ,
    verbose:bool=False, debug:bool=False, output_id:bool=False, progress:bool=False,
    progressbar: str = "") -> models.INGREDIENTS :
    db = Prisma()
    await db.connect()
    if type(ingredient) is dict:
        # Create a new Ingredient
        # print(ingredient)
        # print(ingredient['recipe_id'])
        # print(type(ingredient['recipe_id']))
        responding_recipe = await db.recipes.find_first(
            where={'slug': ingredient['recipe_id']}
        )
        # print(responding_recipe)
        if responding_recipe is not None:
            ingredient['recipe_id'] = responding_recipe.id
        if type(ingredient['comment']) == float:
            ingredient['comment'] = ""
        if type(ingredient['quantity']) == float:
            ingredient['quantity'] = ""
        if type(ingredient['display']) == float:
            ingredient['display'] = ""
        
        # new_ingredient_input = types.INGREDIENTSCreateInput(**ingredient)
        upsert_ingredient_input = types.INGREDIENTSUpsertInput(
            create=types.INGREDIENTSCreateInput(**ingredient),update=types.INGREDIENTSUpdateInput(**ingredient))

    # elif type(ingredient) is RECIPESWithoutId:
    #     new_ingredient_input = types.RECIPESCreateInput(**json.loads(ingredient.json()))
    else:
        raise TypeError("ingredient must be a dict") # or RECIPESWithoutId")
    new_ingredient = await db.ingredients.upsert(
        where={'id': ingredient['id']},
        data=upsert_ingredient_input
    )
    if verbose:
        print(f'created recipe: {new_ingredient.json(indent=2)}')

    if debug:
        found = await db.ingredients.find_many(where={'id': new_ingredient.id})
        assert found is not None
        for found_recipe in found:
            print(f'found recipe: {found_recipe.json(indent=2)}')
    if output_id:
        if (progress):
            print(f'{progressbar} {new_ingredient.id}')
        else:
            print(f'{new_ingredient.id}')
    await db.disconnect()
    return new_ingredient

async def check_if_slug_present(slug: str) -> bool:
    db = Prisma()
    await db.connect()
    found = await db.recipes.find_first(where={'slug': slug})        
    # print(found)
    await db.disconnect()
    if found is not None:
        return True
    return False


if __name__ == '__main__':
    filename="ingredients.csv"
    filename2="dishes_tags_reworked.csv"
    mod_path = Path(__file__).parent
    dataset_abs_path = (mod_path / filename).resolve()
    df = pd.read_csv(fr'{dataset_abs_path}')
    df2 = pd.read_csv(fr'{mod_path / filename2}')
    #drop row if df['recipe_id'] is not in df2['slug']
    df = df[df['recipe_id'].isin(df2['slug'])]

    df_len = len(df.index)
    rows = df.itertuples(index=False)
    ingredient = {}
    debug = False
    if 'debug' in args or '--debug' in args:
        debug = True
    short = False
    counter = 1
    if 'short' in args or '--short' in args:
        short = True
        df_len = 100
    loop = asyncio.get_event_loop()
    for row in rows:
        # change row into dict
        ingredient = row._asdict() 
        if short:
            if counter > 100:
                break
        if counter < 218:
            counter+=1
            continue
        db = Prisma()
        Should_add_ingredient=loop.run_until_complete(check_if_slug_present(ingredient['recipe_id']))
        if not Should_add_ingredient:
            print(f"no matching recipes for slug:{ingredient['recipe_id']}")
            counter+=1
            continue
        asyncio.run(import_ingredient(ingredient, output_id=True, progress=True, progressbar=str(f'{counter}/{df_len}:')))
        counter+=1
    loop.close()
    print("imported recipes complete")