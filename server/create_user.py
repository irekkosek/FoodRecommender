import asyncio
from hmac import new
from os import name
import re
from numpy import rec
from prisma import Prisma, types
import pandas as pd
from pathlib import Path

async def create_user_likes(userid : int = 1, verbose = False, debug = False, output_id=False) -> None:
    db = Prisma()
    await db.connect()
    new_user = await db.users.create(
        {
            'id': userid,
            'name': 'test',
            'password' : 'test'
        }
    )
    if verbose:
        print(f'created recipe: {new_user.json(indent=2)}')

    if debug:
        found = await db.users.find_many(where={'id': userid})
        assert found is not None
        for found_like in found:
            print(f'found like: {found_like.json(indent=2)}')
    if output_id:
        print(f'{new_user.id}')
    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(create_user_likes(verbose=True, debug=True, output_id=True))
