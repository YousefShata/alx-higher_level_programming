#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  fs.writeFile(path, body, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    }
    if (data) {
      console.log(data);
    }
  });
});
