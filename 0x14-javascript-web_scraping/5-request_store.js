#!/usr/bin/node
const argv1 = process.argv[2];
const argv2 = process.argv[3];
const req = require('request');
const fs = require('fs');

req.get(argv1, function (err, response) {
  if (err) throw err;
  fs.appendFile(argv2, response.body, function (err) {
    if (err) throw err;
  });
});
