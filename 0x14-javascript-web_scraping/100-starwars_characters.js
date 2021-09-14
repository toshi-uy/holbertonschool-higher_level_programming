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
    function sortObjectByKeys(o) {
      return Object.keys(o).sort().reduce((r, k) => (r[k] = o[k], r), {});
    }
    var sorted=sortObjectByKeys(body.characters);
    sorted.forEach(element => {
      request(element, options, (error, res, body) => {
        if (error) {
          return console.log(error);
        }
        if (!error && res.statusCode === 200) {
          console.log(body.name);
        }
      });
    });
  }
});
