#!/bin/sh

set -e

CONTAINER_ALREADY_STARTED="/.container_already_started"
if [ ! -e $CONTAINER_ALREADY_STARTED ]; then
    touch $CONTAINER_ALREADY_STARTED
    echo "-- First container startup --"
    echo "-- Running prisma db push --"
    prisma db push --force-reset --accept-data-loss 
    echo "-- Running prisma generate --"
    prisma generate 
    echo "-- running import_recipes.py--"
    python import_recipes.py --short
    echo "-- running create_user.py--"
    python create_user.py 
    echo "-- running create_user_likes.py--"
    python create_user_likes.py
    echo "-- Finished setup--"
else
    echo "-- Not first container startup --"
fi
exec "$@"


