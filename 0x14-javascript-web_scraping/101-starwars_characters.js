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
    let unsorted = body.characters;
    console.log(unsorted);
    for (let i = 0; i < unsorted.length; i++) {
      request(unsorted[i], options, (error, res, body) => {
        if (error) {
          return console.log(error);
        }
        if (!error && res.statusCode === 200) {
          console.log(body.name);
          console.log(unsorted[i]);
        }
      })
    }
  }
});
