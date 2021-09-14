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
    const unsorted = body.characters;
    let sorted = [];
    for (let i = 0; i < unsorted.length; i++) {
      sorted.push(unsorted[i]);
    }
    sorted = sorted.sort()
    for (let i = 0; i < sorted.length; i++) {
      request(sorted[i], options, (error, res, body) => {
        if (error) {
          return console.log(error);
        }
        if (!error && res.statusCode === 200) {
          console.log(body.name);
          console.log(sorted[i]);
        }
      })
    }
  }
});
