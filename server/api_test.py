import json

from numpy import rec
from tokenize import String

from numpy import rec
from import_recipes import import_recipes

async def test_creating():
    recipe_json = "{\"id\": 868,\"name\": \"Homemade Cinnamon Rolls\", \"slug\": \"homemade-cinnamon-rolls\", \"video_url\": \"https://vid.tasty.co/output/25812/mp4_640x640/1488912074\", \"thumbnail_url\": \"https://img.buzzfeed.com/video-api-prod/assets/9d589367531e4c12a4937e30e521c865/fbthumb.jpg\", \"ratings_negative\": 475, \"ratings_positive\": 17340, \"score\": 98, \"cooking_style_big_batch\": 1, \"cooking_style_kid_friendly\": 1, \"cooking_style_bake\": 1, \"meal_breakfast\": 1, \"meal_bakery_goods\": 1, \"cuisine_american\": 1, \"meal_drinks\": 0, \"difficulty_5_ingredients_or_less\": 0, \"healthy_low_calorie\": 0, \"difficulty_easy\": 0, \"dietary_gluten_free\": 0, \"dietary_vegetarian\": 0, \"difficulty_under_1_hour\": 0, \"difficulty_under_45_minutes\": 0, \"healthy_high_protein\": 0, \"dietary_kid_friendly\": 1, \"cuisine_fusion\": 0, \"method_steam\": 0, \"cuisine_japanese\": 0, \"dietary_comfort_food\": 0, \"dietary_indulgent_sweets\": 1, \"method_bake\": 1, \"dietary_dairy_free\": 0, \"cooking_style_one_pot_or_pan\": 0, \"cooking_style_pan_fry\": 0, \"dietary_healthy\": 0, \"method_pan_fry\": 0, \"healthy_low_fat\": 0, \"healthy_low_sugar\": 0, \"healthy_low_carb\": 0, \"cooking_style_mashup\": 0, \"meal_snacks\": 0, \"seasonal_winter\": 0, \"cuisine_british\": 0, \"cooking_style_comfort_food\": 0, \"healthy_high_fiber\": 0, \"cuisine_french\": 0, \"meal_desserts\": 0, \"difficulty_under_15_minutes\": 0, \"difficulty_under_30_minutes\": 0, \"dietary_keto\": 0, \"seasonal_summer\": 0, \"cooking_style_no_bake_desserts\": 0, \"dietary_vegan\": 0, \"cuisine_mexican\": 0, \"seasonal_spring\": 0, \"cuisine_italian\": 0, \"meal_lunch\": 0, \"seasonal_fall\": 0, \"cuisine_german\": 0, \"cooking_style_meal_prep\": 0, \"meal_dinner\": 0, \"meal_appetizers\": 0, \"meal_sides\": 0, \"cuisine_african\": 0, \"cuisine_middle_eastern\": 0, \"method_deep_fry\": 0, \"cuisine_latin_american\": 0, \"method_grill\": 0, \"cuisine_dominican\": 0, \"dietary_pescatarian\": 0, \"cuisine_seafood\": 0, \"cuisine_chinese\": 0, \"cuisine_greek\": 0, \"dietary_contains_alcohol\": 0, \"cuisine_indian\": 0, \"cooking_style_steam\": 0, \"cooking_style_stuffed\": 0, \"cuisine_caribbean\": 0, \"cuisine_filipino\": 0, \"cuisine_taiwanese\": 0, \"cuisine_korean\": 0, \"cuisine_jamaican\": 0, \"meal_brunch\": 0, \"cuisine_swedish\": 0, \"cooking_style_deep_fry\": 0, \"cuisine_west_african\": 0, \"cuisine_thai\": 0, \"cuisine_vietnamese\": 0, \"cuisine_peruvian\": 0, \"cuisine_brazilian\": 0, \"cooking_style_grill\": 0, \"cuisine_bbq\": 0, \"cuisine_kenyan\": 0, \"cuisine_haitian\": 0, \"cuisine_persian\": 0, \"cuisine_ethiopian\": 0, \"cuisine_cuban\": 0, \"cuisine_puerto_rican\": 0, \"cuisine_soul_food\": 0, \"cuisine_indigenous\": 0, \"cuisine_laotian\": 0, \"cuisine_hawaiian\": 0, \"method_no_bake_desserts\": 0, \"cuisine_lebanese\": 0, \"cuisine_south_african\": 0, \"cuisine_venezuelan\": 0}"
    recipe = json.loads(recipe_json)
    print(json.dumps(recipe,indent=2))
    # if type(recipe['id']) is str:
    #     recipe['id'] = int(recipe['id'])
    result = await import_recipes(recipe, verbose=True, debug=True, output_id=True)
    

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_creating())
    loop.close()