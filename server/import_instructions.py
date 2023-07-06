import asyncio
from doctest import debug
from os import name
import re
from numpy import rec
from prisma import Prisma, types
import pandas as pd
from pathlib import Path
import sys

args = sys.argv

async def import_instructions(instruction: dict, verbose:bool=False, debug:bool=False, output_id:bool=False) -> None:
    db = Prisma()
    await db.connect()
    # Create a new instruction
    new_instruction = await db.instructions.create(
        {
            'id': instruction['id'],
            'step': instruction['step'],
            'step_number': instruction['step_number'],
            'recipe_id': instruction['recipe_id']
        }
         
    )
    if verbose:
        print(f'created instruction: {new_instruction.json(indent=2)}')

    if debug:
        found = await db.instructions.find_many(where={'id': new_instruction.id})
        assert found is not None
        for found_instruction in found:
            print(f'found instruction: {found_instruction.json(indent=2)}')
    if output_id:
        print(f'{new_instruction.id}')

    await db.disconnect()
filename="instructions.csv"
mod_path = Path(__file__).parent
dataset_abs_path = (mod_path / filename).resolve()
df = pd.read_csv(fr'{dataset_abs_path}')

rows = df.itertuples() #(index=False)
instruction = {}
debug = False
if 'debug' in args or '--debug' in args:
    debug = True
short = False
counter = 0
if 'short' in args or '--short' in args:
    short = True

for row in rows:
    # change row into dict
    instruction = row._asdict() 
    if short:
        counter+=1
        if counter > 100:
            break
    asyncio.run(import_instructions(instruction, output_id=True))
 
print("imported instructions complete")
    



