#!/usr/bin/node
const argv1 = process.argv[1];
const argv2 = process.argv[2];
const req = require('request');
const fs = require('fs');

request.get(argv1, function (err, response) {
  if (err) throw err;
  fs.appendFile(response.body, argv2, function (err) {
    if (err) throw err;
  });
});
