#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const options = { json: true };
let dict = {}
request(url, options, (error, res, body) => {
  if (error) {
    return console.log(error);
  }
  if (!error && res.statusCode === 200) {
    body.forEach(tasks => {
      tasks.forEach(element => {
        if (tasks.completed === true)
          dict.push({
            user = tasks.userId,
            completed = true
          })
      });
    });
    console.log(dict)
  }
});
