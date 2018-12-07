
FROM nginx:1.13.3-alpine

# RUN apt-get install bash

## Copy our default nginx config
COPY ./default.conf /etc/nginx/conf.d/

## Remove default nginx website
RUN rm -rf /usr/share/nginx/html/*
RUN mkdir -p /usr/share/nginx/angular

## From 'builder' stage copy over the artifacts in dist folder to default nginx public folder
# COPY /ng-app/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
