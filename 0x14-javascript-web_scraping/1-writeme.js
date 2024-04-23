#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv[2];
const input = process.argv[3];

fs.writeFile(fileName, input, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
  if (data) {
    console.log(data);
  }
});
