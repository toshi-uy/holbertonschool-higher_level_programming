#!/usr/bin/node
const filmNbr = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films' + filmNbr
const q = request.parse(url, true);
console.log(q.title);
