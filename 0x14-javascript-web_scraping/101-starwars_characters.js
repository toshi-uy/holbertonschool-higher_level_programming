#!/usr/bin/node
const filmNbr = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + filmNbr;
const options = { json: true };
request(url, options, (error, res, body) => {
  if (error) {
    return console.log(error);
  }
  if (!error && res.statusCode === 200) {
    const sorted = JSON.parse(body).characters;
    sorted.forEach(element => {
      request(sorted[i], (error, res, body) => {
        if (error) {
          return console.log(error);
        }
        if (!error && res.statusCode === 200) {
          const name = JSON.parse(body).name;
          console.log(name);
        }
    })
    });
    }
  });
