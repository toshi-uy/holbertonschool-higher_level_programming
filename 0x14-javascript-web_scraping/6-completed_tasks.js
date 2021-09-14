#!/usr/bin/node
const url = 'https://jsonplaceholder.typicode.com/todos';
const request = require('request');
const options = { json: true };
request(url, options, (error, res, body) => {
  if (error) {
    return console.log(error);
  }
  if (!error && res.statusCode === 200) {
    body.results.forEach(element => { 
      console.log(element);
    });
  }
});