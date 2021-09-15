#!/usr/bin/node
const filmNbr = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + filmNbr;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const path = JSON.parse(body).characters;
  console.log(path);
  let wholeArray = Object.keys(path).map(key => path[key]);
  console.log(wholeArray);

  for(i = 0; i < wholeArray.length; i++) {
    request(wholeArray[i], function (error, response, body) {
      if (error) {
        console.error(error);
      }
      const name = JSON.parse(body).name;
      console.log(name);
    });
  };
});
