#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const movieData = JSON.parse(body);
  if (response.statusCode === 200) {
    console.log(movieData.title);
  } else {
    console.log('ERROR');
  }
});
