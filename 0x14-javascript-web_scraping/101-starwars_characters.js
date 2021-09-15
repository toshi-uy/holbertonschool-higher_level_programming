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
  result = [];
  for(let i in path){
    result.push([i, path[i]]);
  }
  console.log(result);

  for(i = 0; i < result.length; i++) {
    request(result[i], function (error, response, body) {
      if (error) {
        console.error(error);
      }
      const name = JSON.parse(body).name;
      console.log(name);
    });
  };
});