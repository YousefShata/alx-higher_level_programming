#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  
  if (response.statusCode === 200) {
   
   const completed = {}
   const tasks = JSON.parse(body)
     for (const task of tasks) {
      if (task.completed) {
      	
      }
  }
});
