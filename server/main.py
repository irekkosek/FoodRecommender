import asyncio
from os import name
import re
from prisma import Prisma

async def main() -> None:
    db = Prisma()
    await db.connect()

    # Create a new recipe
    recipe = await db.recpies.create({
        'id': 1,
        'name': "Cinnamon Roll Coffee Cake",
        'slug': "cinnamon-roll-coffee-cake",
        'thumbnail_url': "https://img.buzzfeed.com/thumbnailer-prod-us-east-1/video-api/assets/449848.jpg?resize=600:*&output-format=auto&output-quality=auto",
    })
    print(f'created recipe: {recipe.json(indent=2)}')

    found = await db.recpies.find_many(where={'id': recipe.id})
    assert found is not None
    for recipe in found:
        print(f'found recipe: {recipe.json(indent=2)}')
    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())



