#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const options = { json: true };
let results = {}
request(url, options, (error, res, body) => {
  if (error) {
    return console.log(error);
  }
  if (!error && res.statusCode === 200) {
    body.forEach(tasks => {
        let count = 1;
        if (tasks.completed)
          if (results[tasks.userId] = NaN)
            results[tasks.userId] += count;
          else
            results[tasks.userId] += count;
    });
    console.log(results)
  }
});
