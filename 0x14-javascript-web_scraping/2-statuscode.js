#!/usr/bin/node
const url = process.argv[2];
var request = require('request');
request.get(url, function (err, response) {
  console.log("Code: " + response.statusCode); 
});
