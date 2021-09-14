#!/usr/bin/node
const filmNbr = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + filmNbr
let rawdata = request.readFileSync(url);
let student = JSON.parse(rawdata);
console.log(student.title);
