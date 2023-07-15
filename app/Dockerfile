FROM node:20 as dev
WORKDIR /app
COPY package.json yarn.lock /app/
RUN  yarn install && yarn cache clean
COPY . /app
CMD ["yarn", "run", "dev", "--host"]
# FROM node as dev 
# WORKDIR /app
# COPY package.json /app/package.json
# RUN npm install
# COPY . /app
# CMD ["npm", "run", "dev"]


