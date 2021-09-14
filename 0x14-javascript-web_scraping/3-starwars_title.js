#!/usr/bin/node
const filmNbr = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films' + filmNbr
request.get(url, function (err, data) {
  if (err) throw err;
  console.log(data.title);
});
