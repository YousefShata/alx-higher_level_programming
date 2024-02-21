#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
