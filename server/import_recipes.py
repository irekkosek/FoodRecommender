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

async def import_recpies(recipe: dict, verbose:bool=False, debug:bool=False, output_id:bool=False) -> None:
    db = Prisma()
    await db.connect()
    # check if video_url is NaN
    if type(recipe['video_url']) is float:
        recipe['video_url'] = None
    # Create a new recipe
    new_recipe = await db.recipes.create(
        {
            'id': recipe['id'],
            'name': recipe['name'],
            'slug': recipe['slug'],
            'video_url': recipe['video_url'],
            'thumbnail_url': recipe['thumbnail_url'],
            'ratings_negative': recipe['ratings_negative'],
            'ratings_positive': recipe['ratings_positive'],
            'score': recipe['score'],
            'cooking_style_big_batch': recipe['cooking_style_big_batch'],
            'cooking_style_kid_friendly': recipe['cooking_style_kid_friendly'],
            'cooking_style_bake': recipe['cooking_style_bake'],
            'meal_breakfast': recipe['meal_breakfast'],
            'meal_bakery_goods': recipe['meal_bakery_goods'],
            'cuisine_american': recipe['cuisine_american'],
            'meal_drinks': recipe['meal_drinks'],
            'difficulty_5_ingredients_or_less': recipe['difficulty_5_ingredients_or_less'],
            'healthy_low_calorie': recipe['healthy_low_calorie'],
            'difficulty_easy': recipe['difficulty_easy'],
            'dietary_gluten_free': recipe['dietary_gluten_free'],
            'dietary_vegetarian': recipe['dietary_vegetarian'],
            'difficulty_under_1_hour': recipe['difficulty_under_1_hour'],
            'difficulty_under_45_minutes': recipe['difficulty_under_45_minutes'],
            'healthy_high_protein': recipe['healthy_high_protein'],
            'dietary_kid_friendly': recipe['dietary_kid_friendly'],
            'cuisine_fusion': recipe['cuisine_fusion'],
            'method_steam': recipe['method_steam'],
            'cuisine_japanese': recipe['cuisine_japanese'],
            'dietary_comfort_food': recipe['dietary_comfort_food'],
            'dietary_indulgent_sweets': recipe['dietary_indulgent_sweets'],
            'method_bake': recipe['method_bake'],
            'dietary_dairy_free': recipe['dietary_dairy_free'],
            'cooking_style_one_pot_or_pan': recipe['cooking_style_one_pot_or_pan'],
            'cooking_style_pan_fry': recipe['cooking_style_pan_fry'],
            'dietary_healthy': recipe['dietary_healthy'],
            'method_pan_fry': recipe['method_pan_fry'],
            'healthy_low_fat': recipe['healthy_low_fat'],
            'healthy_low_sugar': recipe['healthy_low_sugar'],
            'healthy_low_carb': recipe['healthy_low_carb'],
            'cooking_style_mashup': recipe['cooking_style_mashup'],
            'meal_snacks': recipe['meal_snacks'],
            'seasonal_winter': recipe['seasonal_winter'],
            'cuisine_british': recipe['cuisine_british'],
            'cooking_style_comfort_food': recipe['cooking_style_comfort_food'],
            'healthy_high_fiber': recipe['healthy_high_fiber'],
            'cuisine_french': recipe['cuisine_french'],
            'meal_desserts': recipe['meal_desserts'],
            'difficulty_under_15_minutes': recipe['difficulty_under_15_minutes'],
            'difficulty_under_30_minutes': recipe['difficulty_under_30_minutes'],
            'dietary_keto': recipe['dietary_keto'],
            'seasonal_summer': recipe['seasonal_summer'],
            'cooking_style_no_bake_desserts': recipe['cooking_style_no_bake_desserts'],
            'dietary_vegan': recipe['dietary_vegan'],
            'cuisine_mexican': recipe['cuisine_mexican'],
            'seasonal_spring': recipe['seasonal_spring'],
            'cuisine_italian': recipe['cuisine_italian'],
            'meal_lunch': recipe['meal_lunch'],
            'seasonal_fall': recipe['seasonal_fall'],
            'cuisine_german': recipe['cuisine_german'],
            'cooking_style_meal_prep': recipe['cooking_style_meal_prep'],
            'meal_dinner': recipe['meal_dinner'],
            'meal_appetizers': recipe['meal_appetizers'],
            'meal_sides': recipe['meal_sides'],
            'cuisine_african': recipe['cuisine_african'],
            'cuisine_middle_eastern': recipe['cuisine_middle_eastern'],
            'method_deep_fry': recipe['method_deep_fry'],
            'cuisine_latin_american': recipe['cuisine_latin_american'],
            'method_grill': recipe['method_grill'],
            'cuisine_dominican': recipe['cuisine_dominican'],
            'dietary_pescatarian': recipe['dietary_pescatarian'],
            'cuisine_seafood': recipe['cuisine_seafood'],
            'cuisine_chinese': recipe['cuisine_chinese'],
            'cuisine_greek': recipe['cuisine_greek'],
            'dietary_contains_alcohol': recipe['dietary_contains_alcohol'],
            'cuisine_indian': recipe['cuisine_indian'],
            'cooking_style_steam': recipe['cooking_style_steam'],
            'cooking_style_stuffed': recipe['cooking_style_stuffed'],
            'cuisine_caribbean': recipe['cuisine_caribbean'],
            'cuisine_filipino': recipe['cuisine_filipino'],
            'cuisine_taiwanese': recipe['cuisine_taiwanese'],
            'cuisine_korean': recipe['cuisine_korean'],
            'cuisine_jamaican': recipe['cuisine_jamaican'],
            'meal_brunch': recipe['meal_brunch'],
            'cuisine_swedish': recipe['cuisine_swedish'],
            'cooking_style_deep_fry': recipe['cooking_style_deep_fry'],
            'cuisine_west_african': recipe['cuisine_west_african'],
            'cuisine_thai': recipe['cuisine_thai'],
            'cuisine_vietnamese': recipe['cuisine_vietnamese'],
            'cuisine_peruvian': recipe['cuisine_peruvian'],
            'cuisine_brazilian': recipe['cuisine_brazilian'],
            'cooking_style_grill': recipe['cooking_style_grill'],
            'cuisine_bbq': recipe['cuisine_bbq'],
            'cuisine_kenyan': recipe['cuisine_kenyan'],
            'cuisine_haitian': recipe['cuisine_haitian'],
            'cuisine_persian': recipe['cuisine_persian'],
            'cuisine_ethiopian': recipe['cuisine_ethiopian'],
            'cuisine_cuban': recipe['cuisine_cuban'],
            'cuisine_puerto_rican': recipe['cuisine_puerto_rican'],
            'cuisine_soul_food': recipe['cuisine_soul_food'],
            'cuisine_indigenous': recipe['cuisine_indigenous'],
            'cuisine_laotian': recipe['cuisine_laotian'],
            'cuisine_hawaiian': recipe['cuisine_hawaiian'],
            'method_no_bake_desserts': recipe['method_no_bake_desserts'],
            'cuisine_lebanese': recipe['cuisine_lebanese'],
            'cuisine_south_african': recipe['cuisine_south_african'],
            'cuisine_venezuelan': recipe['cuisine_venezuelan']
        }
         
    )
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
    asyncio.run(import_recpies(recipe, output_id=True))
 
print("imported recipes complete")
    



