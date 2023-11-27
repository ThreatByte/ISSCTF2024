FROM node:latest
WORKDIR /usr/src/app
COPY package*.json ./
COPY server.js ./
RUN npm install

EXPOSE 3000

ENV NODE_ENV=production

CMD ["node", "server.js"]
