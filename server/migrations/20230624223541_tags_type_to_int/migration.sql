/*
  Warnings:

  - The `ratings_negative` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `ratings_positive` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `score` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cooking_style_big_batch` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cooking_style_kid_friendly` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cooking_style_bake` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `meal_breakfast` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `meal_bakery_goods` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_american` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `meal_drinks` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `difficulty_5_ingredients_or_less` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `healthy_low_calorie` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `difficulty_easy` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `dietary_gluten_free` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `dietary_vegetarian` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `difficulty_under_1_hour` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `difficulty_under_45_minutes` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `healthy_high_protein` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `dietary_kid_friendly` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_fusion` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `method_steam` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_japanese` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `dietary_comfort_food` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `dietary_indulgent_sweets` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `method_bake` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `dietary_dairy_free` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cooking_style_one_pot_or_pan` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cooking_style_pan_fry` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `dietary_healthy` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `method_pan_fry` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `healthy_low_fat` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `healthy_low_sugar` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `healthy_low_carb` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cooking_style_mashup` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `meal_snacks` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `seasonal_winter` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_british` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cooking_style_comfort_food` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `healthy_high_fiber` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_french` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `meal_desserts` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `difficulty_under_15_minutes` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `difficulty_under_30_minutes` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `dietary_keto` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `seasonal_summer` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cooking_style_no_bake_desserts` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `dietary_vegan` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_mexican` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `seasonal_spring` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_italian` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `meal_lunch` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `seasonal_fall` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_german` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cooking_style_meal_prep` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `meal_dinner` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `meal_appetizers` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `meal_sides` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_african` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_middle_eastern` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `method_deep_fry` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_latin_american` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `method_grill` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_dominican` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `dietary_pescatarian` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_seafood` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_chinese` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_greek` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `dietary_contains_alcohol` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_indian` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cooking_style_steam` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cooking_style_stuffed` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_caribbean` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_filipino` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_taiwanese` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_korean` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_jamaican` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `meal_brunch` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_swedish` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cooking_style_deep_fry` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_west_african` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_thai` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_vietnamese` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_peruvian` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_brazilian` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cooking_style_grill` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_bbq` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_kenyan` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_haitian` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_persian` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_ethiopian` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_cuban` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_puerto_rican` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_soul_food` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_indigenous` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_laotian` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_hawaiian` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `method_no_bake_desserts` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_lebanese` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_south_african` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.
  - The `cuisine_venezuelan` column on the `RECPIES` table would be dropped and recreated. This will lead to data loss if there is data in the column.

*/
-- AlterTable
ALTER TABLE "RECPIES" DROP COLUMN "ratings_negative",
ADD COLUMN     "ratings_negative" INTEGER DEFAULT 0,
DROP COLUMN "ratings_positive",
ADD COLUMN     "ratings_positive" INTEGER DEFAULT 0,
DROP COLUMN "score",
ADD COLUMN     "score" INTEGER DEFAULT 0,
DROP COLUMN "cooking_style_big_batch",
ADD COLUMN     "cooking_style_big_batch" INTEGER DEFAULT 0,
DROP COLUMN "cooking_style_kid_friendly",
ADD COLUMN     "cooking_style_kid_friendly" INTEGER DEFAULT 0,
DROP COLUMN "cooking_style_bake",
ADD COLUMN     "cooking_style_bake" INTEGER DEFAULT 0,
DROP COLUMN "meal_breakfast",
ADD COLUMN     "meal_breakfast" INTEGER DEFAULT 0,
DROP COLUMN "meal_bakery_goods",
ADD COLUMN     "meal_bakery_goods" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_american",
ADD COLUMN     "cuisine_american" INTEGER DEFAULT 0,
DROP COLUMN "meal_drinks",
ADD COLUMN     "meal_drinks" INTEGER DEFAULT 0,
DROP COLUMN "difficulty_5_ingredients_or_less",
ADD COLUMN     "difficulty_5_ingredients_or_less" INTEGER DEFAULT 0,
DROP COLUMN "healthy_low_calorie",
ADD COLUMN     "healthy_low_calorie" INTEGER DEFAULT 0,
DROP COLUMN "difficulty_easy",
ADD COLUMN     "difficulty_easy" INTEGER DEFAULT 0,
DROP COLUMN "dietary_gluten_free",
ADD COLUMN     "dietary_gluten_free" INTEGER DEFAULT 0,
DROP COLUMN "dietary_vegetarian",
ADD COLUMN     "dietary_vegetarian" INTEGER DEFAULT 0,
DROP COLUMN "difficulty_under_1_hour",
ADD COLUMN     "difficulty_under_1_hour" INTEGER DEFAULT 0,
DROP COLUMN "difficulty_under_45_minutes",
ADD COLUMN     "difficulty_under_45_minutes" INTEGER DEFAULT 0,
DROP COLUMN "healthy_high_protein",
ADD COLUMN     "healthy_high_protein" INTEGER DEFAULT 0,
DROP COLUMN "dietary_kid_friendly",
ADD COLUMN     "dietary_kid_friendly" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_fusion",
ADD COLUMN     "cuisine_fusion" INTEGER DEFAULT 0,
DROP COLUMN "method_steam",
ADD COLUMN     "method_steam" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_japanese",
ADD COLUMN     "cuisine_japanese" INTEGER DEFAULT 0,
DROP COLUMN "dietary_comfort_food",
ADD COLUMN     "dietary_comfort_food" INTEGER DEFAULT 0,
DROP COLUMN "dietary_indulgent_sweets",
ADD COLUMN     "dietary_indulgent_sweets" INTEGER DEFAULT 0,
DROP COLUMN "method_bake",
ADD COLUMN     "method_bake" INTEGER DEFAULT 0,
DROP COLUMN "dietary_dairy_free",
ADD COLUMN     "dietary_dairy_free" INTEGER DEFAULT 0,
DROP COLUMN "cooking_style_one_pot_or_pan",
ADD COLUMN     "cooking_style_one_pot_or_pan" INTEGER DEFAULT 0,
DROP COLUMN "cooking_style_pan_fry",
ADD COLUMN     "cooking_style_pan_fry" INTEGER DEFAULT 0,
DROP COLUMN "dietary_healthy",
ADD COLUMN     "dietary_healthy" INTEGER DEFAULT 0,
DROP COLUMN "method_pan_fry",
ADD COLUMN     "method_pan_fry" INTEGER DEFAULT 0,
DROP COLUMN "healthy_low_fat",
ADD COLUMN     "healthy_low_fat" INTEGER DEFAULT 0,
DROP COLUMN "healthy_low_sugar",
ADD COLUMN     "healthy_low_sugar" INTEGER DEFAULT 0,
DROP COLUMN "healthy_low_carb",
ADD COLUMN     "healthy_low_carb" INTEGER DEFAULT 0,
DROP COLUMN "cooking_style_mashup",
ADD COLUMN     "cooking_style_mashup" INTEGER DEFAULT 0,
DROP COLUMN "meal_snacks",
ADD COLUMN     "meal_snacks" INTEGER DEFAULT 0,
DROP COLUMN "seasonal_winter",
ADD COLUMN     "seasonal_winter" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_british",
ADD COLUMN     "cuisine_british" INTEGER DEFAULT 0,
DROP COLUMN "cooking_style_comfort_food",
ADD COLUMN     "cooking_style_comfort_food" INTEGER DEFAULT 0,
DROP COLUMN "healthy_high_fiber",
ADD COLUMN     "healthy_high_fiber" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_french",
ADD COLUMN     "cuisine_french" INTEGER DEFAULT 0,
DROP COLUMN "meal_desserts",
ADD COLUMN     "meal_desserts" INTEGER DEFAULT 0,
DROP COLUMN "difficulty_under_15_minutes",
ADD COLUMN     "difficulty_under_15_minutes" INTEGER DEFAULT 0,
DROP COLUMN "difficulty_under_30_minutes",
ADD COLUMN     "difficulty_under_30_minutes" INTEGER DEFAULT 0,
DROP COLUMN "dietary_keto",
ADD COLUMN     "dietary_keto" INTEGER DEFAULT 0,
DROP COLUMN "seasonal_summer",
ADD COLUMN     "seasonal_summer" INTEGER DEFAULT 0,
DROP COLUMN "cooking_style_no_bake_desserts",
ADD COLUMN     "cooking_style_no_bake_desserts" INTEGER DEFAULT 0,
DROP COLUMN "dietary_vegan",
ADD COLUMN     "dietary_vegan" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_mexican",
ADD COLUMN     "cuisine_mexican" INTEGER DEFAULT 0,
DROP COLUMN "seasonal_spring",
ADD COLUMN     "seasonal_spring" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_italian",
ADD COLUMN     "cuisine_italian" INTEGER DEFAULT 0,
DROP COLUMN "meal_lunch",
ADD COLUMN     "meal_lunch" INTEGER DEFAULT 0,
DROP COLUMN "seasonal_fall",
ADD COLUMN     "seasonal_fall" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_german",
ADD COLUMN     "cuisine_german" INTEGER DEFAULT 0,
DROP COLUMN "cooking_style_meal_prep",
ADD COLUMN     "cooking_style_meal_prep" INTEGER DEFAULT 0,
DROP COLUMN "meal_dinner",
ADD COLUMN     "meal_dinner" INTEGER DEFAULT 0,
DROP COLUMN "meal_appetizers",
ADD COLUMN     "meal_appetizers" INTEGER DEFAULT 0,
DROP COLUMN "meal_sides",
ADD COLUMN     "meal_sides" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_african",
ADD COLUMN     "cuisine_african" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_middle_eastern",
ADD COLUMN     "cuisine_middle_eastern" INTEGER DEFAULT 0,
DROP COLUMN "method_deep_fry",
ADD COLUMN     "method_deep_fry" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_latin_american",
ADD COLUMN     "cuisine_latin_american" INTEGER DEFAULT 0,
DROP COLUMN "method_grill",
ADD COLUMN     "method_grill" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_dominican",
ADD COLUMN     "cuisine_dominican" INTEGER DEFAULT 0,
DROP COLUMN "dietary_pescatarian",
ADD COLUMN     "dietary_pescatarian" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_seafood",
ADD COLUMN     "cuisine_seafood" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_chinese",
ADD COLUMN     "cuisine_chinese" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_greek",
ADD COLUMN     "cuisine_greek" INTEGER DEFAULT 0,
DROP COLUMN "dietary_contains_alcohol",
ADD COLUMN     "dietary_contains_alcohol" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_indian",
ADD COLUMN     "cuisine_indian" INTEGER DEFAULT 0,
DROP COLUMN "cooking_style_steam",
ADD COLUMN     "cooking_style_steam" INTEGER DEFAULT 0,
DROP COLUMN "cooking_style_stuffed",
ADD COLUMN     "cooking_style_stuffed" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_caribbean",
ADD COLUMN     "cuisine_caribbean" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_filipino",
ADD COLUMN     "cuisine_filipino" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_taiwanese",
ADD COLUMN     "cuisine_taiwanese" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_korean",
ADD COLUMN     "cuisine_korean" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_jamaican",
ADD COLUMN     "cuisine_jamaican" INTEGER DEFAULT 0,
DROP COLUMN "meal_brunch",
ADD COLUMN     "meal_brunch" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_swedish",
ADD COLUMN     "cuisine_swedish" INTEGER DEFAULT 0,
DROP COLUMN "cooking_style_deep_fry",
ADD COLUMN     "cooking_style_deep_fry" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_west_african",
ADD COLUMN     "cuisine_west_african" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_thai",
ADD COLUMN     "cuisine_thai" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_vietnamese",
ADD COLUMN     "cuisine_vietnamese" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_peruvian",
ADD COLUMN     "cuisine_peruvian" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_brazilian",
ADD COLUMN     "cuisine_brazilian" INTEGER DEFAULT 0,
DROP COLUMN "cooking_style_grill",
ADD COLUMN     "cooking_style_grill" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_bbq",
ADD COLUMN     "cuisine_bbq" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_kenyan",
ADD COLUMN     "cuisine_kenyan" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_haitian",
ADD COLUMN     "cuisine_haitian" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_persian",
ADD COLUMN     "cuisine_persian" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_ethiopian",
ADD COLUMN     "cuisine_ethiopian" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_cuban",
ADD COLUMN     "cuisine_cuban" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_puerto_rican",
ADD COLUMN     "cuisine_puerto_rican" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_soul_food",
ADD COLUMN     "cuisine_soul_food" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_indigenous",
ADD COLUMN     "cuisine_indigenous" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_laotian",
ADD COLUMN     "cuisine_laotian" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_hawaiian",
ADD COLUMN     "cuisine_hawaiian" INTEGER DEFAULT 0,
DROP COLUMN "method_no_bake_desserts",
ADD COLUMN     "method_no_bake_desserts" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_lebanese",
ADD COLUMN     "cuisine_lebanese" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_south_african",
ADD COLUMN     "cuisine_south_african" INTEGER DEFAULT 0,
DROP COLUMN "cuisine_venezuelan",
ADD COLUMN     "cuisine_venezuelan" INTEGER DEFAULT 0;
