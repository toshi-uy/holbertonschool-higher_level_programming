#!/usr/bin/node
const filmNbr = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films' + filmNbr
request.get(url, function (err, body) {
  if (err) throw err;
  console.log(body.title);
});
