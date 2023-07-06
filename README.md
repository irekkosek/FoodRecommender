# food-recommender

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Type Support for `.vue` Imports in TS

TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking. In editors, we need [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin) to make the TypeScript language service aware of `.vue` types.

If the standalone TypeScript plugin doesn't feel fast enough to you, Volar has also implemented a [Take Over Mode](https://github.com/johnsoncodehk/volar/discussions/471#discussioncomment-1361669) that is more performant. You can enable it by the following steps:

1. Disable the built-in TypeScript Extension
   1. Run `Extensions: Show Built-in Extensions` from VSCode's command palette
   2. Find `TypeScript and JavaScript Language Features`, right click and select `Disable (Workspace)`
2. Reload the VSCode window by running `Developer: Reload Window` from the command palette.

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

# Vue:
## Project Setup

for development with npm
```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```

### Run Unit Tests with [Vitest](https://vitest.dev/)

```sh
npm run test:unit
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```
# Python:
## requirements
- python 3.9
- pip
- docker (this can be the only requirement if you plan to use docker for development)

## Project Setup
Supported arguments:
```
CLEAN_DB=true # will drop all tables and recreate them
SEED_DB=true # will seed the database with recipes
SHORT_DB=true # will seed the database with 100 recipes
```
To start project you can use all or selected above arguments with docker-compose up
```sh
CLEAN_DB=true SEED_DB=true SHORT_DB=true docker compose up
```
or you can supply them in .env file in root folder

and when coming back again just run 
```sh
docker-compose up
```
if you wish to run the server in detached mode just add -d to the end of the command
```sh
docker-compose up -d
```

if you wish to run everything locally you can follow these steps:

```sh
cd server && python -m venv venv
pip install -r requirements.txt
prisma db push
```
you can read more about prisma [here](https://prisma-client-py.readthedocs.io/en/stable/getting_started/setup/)

to seed the database
```sh
python import_recipes.py
python create_user.py
python create_user_likes.py
```
you can check the database with [prisma studio](https://www.prisma.io/studio)
just run
```sh
prisma studio
```
to run the example in main
```sh
python main.py
```

to run the server
```sh
uvicorn main:app --reload
```

you can find additional information about it [here](https://fastapi.tiangolo.com/tutorial/first-steps/)

you can also find: 
automatic interactive API documentation (provided by Swagger UI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
alternative automatic documentation (provided by ReDoc): [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

