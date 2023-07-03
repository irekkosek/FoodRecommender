import asyncio
from hmac import new
from os import name
import re
from sqlite3 import connect
from numpy import rec
from prisma import Prisma, types
import pandas as pd
from pathlib import Path

async def create_user_likes(userid : int = 1, recipeid : int = 868, verbose = False, debug = False, output_id=False) -> None:
    db = Prisma()
    await db.connect()
    new_user_like = await db.user_likes_recipes.create(
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
        print(f'created user_like: {new_user_like.json(indent=2)}')

    if debug:
        found = await db.user_likes_recipes.find_many(where={'USER_id': userid})
        assert found is not None
        for found_like in found:
            print(f'found like: {found_like.json(indent=2)}')
    if output_id:
        print(f'{new_user_like.RECIPE_id}, {new_user_like.USER_id}')
        print(f'{new_user_like.recipe}')
    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(create_user_likes(verbose=True, debug=True, output_id=True))
