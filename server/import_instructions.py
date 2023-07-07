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


async def import_instruction(instruction: dict  ,
    verbose:bool=False, debug:bool=False, output_id:bool=False, progress:bool=False,
    progressbar: str = "") -> models.INSTRUCTIONS :
    db = Prisma()
    await db.connect()
    if type(instruction) is dict:
        # Create a new instruction
        # print(instruction)
        # print(instruction['recipe_id'])
        # print(type(instruction['recipe_id']))
        responding_recipe = await db.recipes.find_first(
            where={'slug': instruction['recipe_id']}
        )
        # print(responding_recipe)
        if responding_recipe is not None:
            instruction['recipe_id'] = responding_recipe.id
        if type(instruction['step']) == float:
            instruction['step'] = ""
        if type(instruction['step_number']) == float:
            instruction['step_number'] = 0

        
        # new_instruction_input = types.INSTRUCTIONSCreateInput(**ingredient)
        upsert_ingredient_input = types.INSTRUCTIONSUpsertInput(
            create=types.INSTRUCTIONSCreateInput(**instruction),update=types.INSTRUCTIONSUpdateInput(**instruction))

    # elif type(instruction) is RECIPESWithoutId:
    #     new_instruction_input = types.RECIPESCreateInput(**json.loads(instruction.json()))
    else:
        raise TypeError("instruction must be a dict") # or RECIPESWithoutId")
    new_instruction = await db.instructions.upsert(
        where={'id': instruction['id']},
        data=upsert_ingredient_input
    )
    if verbose:
        print(f'created recipe: {new_instruction.json(indent=2)}')

    if debug:
        found = await db.instructions.find_many(where={'id': new_instruction.id})
        assert found is not None
        for found_recipe in found:
            print(f'found recipe: {found_recipe.json(indent=2)}')
    if output_id:
        if (progress):
            print(f'{progressbar} {new_instruction.id}')
        else:
            print(f'{new_instruction.id}')
    await db.disconnect()
    return new_instruction

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
    filename="instructions.csv"
    filename2="dishes_tags_reworked.csv"
    mod_path = Path(__file__).parent
    dataset_abs_path = (mod_path / filename).resolve()
    df = pd.read_csv(fr'{dataset_abs_path}')
    df2 = pd.read_csv(fr'{mod_path / filename2}')
    #drop row if df['recipe_id'] is not in df2['slug']
    df = df[df['recipe_id'].isin(df2['slug'])]

    df_len = len(df.index)
    rows = df.itertuples(index=False)
    instruction = {}
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
        instruction = row._asdict() 
        if short:
            if counter > 100:
                break
        if counter < 218:
            counter+=1
            continue
        db = Prisma()
        Should_add_instruction=loop.run_until_complete(check_if_slug_present(instruction['recipe_id']))
        if not Should_add_instruction:
            print(f"no matching recipes for slug:{instruction['recipe_id']}")
            counter+=1
            continue
        asyncio.run(import_instruction(instruction, output_id=True, progress=True, progressbar=str(f'{counter}/{df_len}:')))
        counter+=1
    loop.close()
    print("imported recipes complete")