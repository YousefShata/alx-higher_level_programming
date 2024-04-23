#!/usr/bin/node
const request = require('request');

const actorId = '18';
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  let totalMovies = 0;
  const movieData = JSON.parse(body);
  if (response.statusCode === 200) {
    movieData.results.forEach(film => {
      film.characters.forEach(characterURL => {
        const urlParts = characterURL.split('/');
        const id = urlParts[urlParts.length - 2];
        if (id === actorId) {
          totalMovies++;
        }
      });
    });
  }
  console.log(totalMovies);
});
