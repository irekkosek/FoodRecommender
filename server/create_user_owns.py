import asyncio
from hmac import new
from os import name
import re
from sqlite3 import connect
from tkinter import N
from numpy import rec
from prisma import Prisma, types
import pandas as pd
from pathlib import Path

async def create_user_owns(userid : int = 1, recipeid : int = 868, verbose = False, debug = False, output_id=False) -> None:
    db = Prisma()
    await db.connect()
    new_user_owns = await db.user_owns_recipes.create(
        {
            'user': {
                'connect': {
                    'id': userid
                }
            },
            'recipe': {
                'connect': {
                    'id': recipeid
                }
            }
        }
    )
    if verbose:
        print(f'created user_owns: {new_user_owns.json(indent=2)}')
        print(f'{new_user_owns.recipe}')

    if debug:
        found = await db.user_owns_recipes.find_many(where={'USER_id': userid})
        assert found is not None
        for found_owns in found:
            print(f'found owns: {found_owns.json(indent=2)}') 
    if output_id:
        print(f'{new_user_owns.RECIPE_id}, {new_user_owns.USER_id}') 
    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(create_user_owns(verbose=False, debug=False, output_id=True))
