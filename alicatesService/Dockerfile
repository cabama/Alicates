FROM node:latest

# Create app directory
RUN mkdir -p /usr/src/alicates
RUN mkdir -p /usr/src/alicates/src
RUN mkdir -p /usr/src/alicates/bin
RUN mkdir -p /usr/src/alicates/public
WORKDIR /usr/src/alicates

# Install Nodemon
RUN npm install -g tsc
RUN npm install -g concurrently
RUN npm install typescript -g
RUN npm install nodemon mocha supervisor -g

# Install Yarn
RUN npm i -g yarn 
RUN chmod +x /usr/local/lib/node_modules/yarn/bin/yarn.js

# COPY PROJECT SETTINGS
ADD package.json /usr/src/alicates
ADD tsconfig.json /usr/src/alicates
ADD src /usr/src/alicates/src

# FINALLY INSTALL PROYECT DEPS
RUN yarn
RUN yarn ci