#!/usr/bin/node
const filmNbr = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + filmNbr
let rawdata = request.readUrl(url, "utf8");
console.log(rawdata);
