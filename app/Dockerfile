FROM node as dev 
WORKDIR /app
COPY package.json /app/package.json
RUN yarn install
COPY . /app
CMD ["yarn", "run", "dev", "--host"]

# FROM node as dev 
# WORKDIR /app
# COPY package.json /app/package.json
# RUN npm install
# COPY . /app
# CMD ["npm", "run", "dev"]


