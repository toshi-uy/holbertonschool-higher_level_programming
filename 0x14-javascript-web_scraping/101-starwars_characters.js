#!/usr/bin/node
const filmNbr = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + filmNbr;

request(url, function (error, res, body) {
  if (error) {
    console.error(error);
  }
  if (!error && res.statusCode === 200){
    const sorted = JSON.parse(body).characters;
    sorted.forEach(element => {
      request(element, function (error, res, body) {
        if (error) {
          console.error(error);
        }
        if (!error && res.statusCode === 200){
        const name = JSON.parse(body).name;
        console.log(name);
      }
      });
    });
  }
});
