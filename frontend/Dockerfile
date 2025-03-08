FROM node:18-alpine
WORKDIR /event_tick_frontend
COPY event_tick_frontend/package.json event_tick_frontend/package-lock.json ./
RUN npm install
COPY ./event_tick_frontend .
