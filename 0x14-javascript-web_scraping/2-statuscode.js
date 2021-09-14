#!/usr/bin/node
const url = process.argv[2];
var request = require('request');
request.get(url, function (response) {
  console.log('Code:', response.statusCode); 
});
