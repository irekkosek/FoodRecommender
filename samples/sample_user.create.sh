curl -X 'POST' \
  'http://localhost:8000/create/user/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 0,
  "name": "string",
  "password": "string",
  "USER_likes_RECIPES": {},
  "USER_owns_RECIPES": {}
}'

#request body:
{
  "id": 0,
  "name": "string",
  "password": "string",
  "USER_likes_RECIPES": {},
  "USER_owns_RECIPES": {}
}