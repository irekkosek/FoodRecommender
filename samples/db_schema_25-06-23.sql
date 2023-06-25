-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public."RECPIES"
(
    id integer NOT NULL DEFAULT nextval('"RECPIES_id_seq"'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    slug text COLLATE pg_catalog."default",
    video_url text COLLATE pg_catalog."default",
    thumbnail_url text COLLATE pg_catalog."default",
    ratings_negative integer DEFAULT 0,
    ratings_positive integer DEFAULT 0,
    score integer DEFAULT 0,
    cooking_style_big_batch integer DEFAULT 0,
    cooking_style_kid_friendly integer DEFAULT 0,
    cooking_style_bake integer DEFAULT 0,
    meal_breakfast integer DEFAULT 0,
    meal_bakery_goods integer DEFAULT 0,
    cuisine_american integer DEFAULT 0,
    meal_drinks integer DEFAULT 0,
    difficulty_5_ingredients_or_less integer DEFAULT 0,
    healthy_low_calorie integer DEFAULT 0,
    difficulty_easy integer DEFAULT 0,
    dietary_gluten_free integer DEFAULT 0,
    dietary_vegetarian integer DEFAULT 0,
    difficulty_under_1_hour integer DEFAULT 0,
    difficulty_under_45_minutes integer DEFAULT 0,
    healthy_high_protein integer DEFAULT 0,
    dietary_kid_friendly integer DEFAULT 0,
    cuisine_fusion integer DEFAULT 0,
    method_steam integer DEFAULT 0,
    cuisine_japanese integer DEFAULT 0,
    dietary_comfort_food integer DEFAULT 0,
    dietary_indulgent_sweets integer DEFAULT 0,
    method_bake integer DEFAULT 0,
    dietary_dairy_free integer DEFAULT 0,
    cooking_style_one_pot_or_pan integer DEFAULT 0,
    cooking_style_pan_fry integer DEFAULT 0,
    dietary_healthy integer DEFAULT 0,
    method_pan_fry integer DEFAULT 0,
    healthy_low_fat integer DEFAULT 0,
    healthy_low_sugar integer DEFAULT 0,
    healthy_low_carb integer DEFAULT 0,
    cooking_style_mashup integer DEFAULT 0,
    meal_snacks integer DEFAULT 0,
    seasonal_winter integer DEFAULT 0,
    cuisine_british integer DEFAULT 0,
    cooking_style_comfort_food integer DEFAULT 0,
    healthy_high_fiber integer DEFAULT 0,
    cuisine_french integer DEFAULT 0,
    meal_desserts integer DEFAULT 0,
    difficulty_under_15_minutes integer DEFAULT 0,
    difficulty_under_30_minutes integer DEFAULT 0,
    dietary_keto integer DEFAULT 0,
    seasonal_summer integer DEFAULT 0,
    cooking_style_no_bake_desserts integer DEFAULT 0,
    dietary_vegan integer DEFAULT 0,
    cuisine_mexican integer DEFAULT 0,
    seasonal_spring integer DEFAULT 0,
    cuisine_italian integer DEFAULT 0,
    meal_lunch integer DEFAULT 0,
    seasonal_fall integer DEFAULT 0,
    cuisine_german integer DEFAULT 0,
    cooking_style_meal_prep integer DEFAULT 0,
    meal_dinner integer DEFAULT 0,
    meal_appetizers integer DEFAULT 0,
    meal_sides integer DEFAULT 0,
    cuisine_african integer DEFAULT 0,
    cuisine_middle_eastern integer DEFAULT 0,
    method_deep_fry integer DEFAULT 0,
    cuisine_latin_american integer DEFAULT 0,
    method_grill integer DEFAULT 0,
    cuisine_dominican integer DEFAULT 0,
    dietary_pescatarian integer DEFAULT 0,
    cuisine_seafood integer DEFAULT 0,
    cuisine_chinese integer DEFAULT 0,
    cuisine_greek integer DEFAULT 0,
    dietary_contains_alcohol integer DEFAULT 0,
    cuisine_indian integer DEFAULT 0,
    cooking_style_steam integer DEFAULT 0,
    cooking_style_stuffed integer DEFAULT 0,
    cuisine_caribbean integer DEFAULT 0,
    cuisine_filipino integer DEFAULT 0,
    cuisine_taiwanese integer DEFAULT 0,
    cuisine_korean integer DEFAULT 0,
    cuisine_jamaican integer DEFAULT 0,
    meal_brunch integer DEFAULT 0,
    cuisine_swedish integer DEFAULT 0,
    cooking_style_deep_fry integer DEFAULT 0,
    cuisine_west_african integer DEFAULT 0,
    cuisine_thai integer DEFAULT 0,
    cuisine_vietnamese integer DEFAULT 0,
    cuisine_peruvian integer DEFAULT 0,
    cuisine_brazilian integer DEFAULT 0,
    cooking_style_grill integer DEFAULT 0,
    cuisine_bbq integer DEFAULT 0,
    cuisine_kenyan integer DEFAULT 0,
    cuisine_haitian integer DEFAULT 0,
    cuisine_persian integer DEFAULT 0,
    cuisine_ethiopian integer DEFAULT 0,
    cuisine_cuban integer DEFAULT 0,
    cuisine_puerto_rican integer DEFAULT 0,
    cuisine_soul_food integer DEFAULT 0,
    cuisine_indigenous integer DEFAULT 0,
    cuisine_laotian integer DEFAULT 0,
    cuisine_hawaiian integer DEFAULT 0,
    method_no_bake_desserts integer DEFAULT 0,
    cuisine_lebanese integer DEFAULT 0,
    cuisine_south_african integer DEFAULT 0,
    cuisine_venezuelan integer DEFAULT 0,
    CONSTRAINT "RECPIES_pkey" PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public."USERS"
(
    id integer NOT NULL DEFAULT nextval('"USERS_id_seq"'::regclass),
    name text COLLATE pg_catalog."default",
    password text COLLATE pg_catalog."default",
    CONSTRAINT "USERS_pkey" PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public."USER_likes_RECPIES"
(
    "USER_id" integer NOT NULL,
    "RECIPE_id" integer NOT NULL,
    CONSTRAINT "USER_likes_RECPIES_pkey" PRIMARY KEY ("USER_id", "RECIPE_id")
);

CREATE TABLE IF NOT EXISTS public._prisma_migrations
(
    id character varying(36) COLLATE pg_catalog."default" NOT NULL,
    checksum character varying(64) COLLATE pg_catalog."default" NOT NULL,
    finished_at timestamp with time zone,
    migration_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    logs text COLLATE pg_catalog."default",
    rolled_back_at timestamp with time zone,
    started_at timestamp with time zone NOT NULL DEFAULT now(),
    applied_steps_count integer NOT NULL DEFAULT 0,
    CONSTRAINT _prisma_migrations_pkey PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public."USER_likes_RECPIES"
    ADD CONSTRAINT "USER_likes_RECPIES_RECIPE_id_fkey" FOREIGN KEY ("RECIPE_id")
    REFERENCES public."RECPIES" (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE RESTRICT;


ALTER TABLE IF EXISTS public."USER_likes_RECPIES"
    ADD CONSTRAINT "USER_likes_RECPIES_USER_id_fkey" FOREIGN KEY ("USER_id")
    REFERENCES public."USERS" (id) MATCH SIMPLE
    ON UPDATE CASCADE
    ON DELETE RESTRICT;

END;