#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const options = { json: true };
let wedge = 0;
request(url, options, (error, res, body) => {
  if (error) {
    return console.log(error);
  }
  if (!error && res.statusCode === 200) {
    body.results.forEach(element => {
      element.characters.forEach(character => {
        if (character.includes === '/18/') {
          wedge += 1;
        }
      });
    });
    console.log(wedge);
  }
});
