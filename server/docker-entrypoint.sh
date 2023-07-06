#!/bin/sh

set -e

# CONTAINER_ALREADY_STARTED="/.container_already_started"
# if [ ! -e $CONTAINER_ALREADY_STARTED ]; then
#     touch $CONTAINER_ALREADY_STARTED
#     echo "-- First container startup --"
#     # echo "-- Running prisma migrate deploy --"
#     # prisma migrate deploy --preview-feature
#     echo "-- Running prisma db push --"
#     prisma db push --force-reset --accept-data-loss 
#     echo "-- Running prisma generate --"
#     prisma generate 
#     echo "-- running import_recipes.py--"
#     python import_recipes.py --short
#     echo "-- running create_user.py--"
#     python create_user.py 
#     echo "-- running create_user_likes.py--"
#     python create_user_likes.py
#     echo "-- Finished setup--"
# else
#     echo "-- Not first container startup --"
#     prisma generate
# fi

# if [ "$PRISMA_WATCH" = true ]
# then
#     echo "-- Running prisma generate --watch --"
#     prisma generate --watch & #this doesn't finish before running server so it doesn't work
# else
#     echo "-- Running prisma generate --"
#     prisma generate 
# fi
prisma generate
if [ "$CLEAN_DB" = true ]
then
    echo "-- Running prisma db push --"
    prisma db push --force-reset --accept-data-loss
else
    echo "-- Using existing database --"
fi
if [ "$SEED_DB" = true ]
then
    echo "-- Seeding database --"
    if [ "$SHORT_DB" = true ]
    then
        echo "-- running import_recipes.py --short --"
        python import_recipes.py --short
    else
        echo "-- running import_recipes.py--"
        python import_recipes.py
    fi
    echo "-- running create_user.py--"
    python create_user.py 
    echo "-- running create_user_likes.py--"
    python create_user_likes.py
    echo "-- Finished setup--"
else
    echo "-- Not seeding database --"
fi
echo "-- Starting server --"
exec "$@"


