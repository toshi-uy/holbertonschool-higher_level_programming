#!/usr/bin/node
const filmNbr = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + filmNbr;

function resolveAfter2Seconds(x) {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(x);
    }, 2000);
  });
}

async function f1() {
  request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const path = JSON.parse(body).characters;
  path.forEach(element => {
    const x = await resolveAfter2Seconds(10);
    request(element, function (error, body) {
      if (error) {
        console.error(error);
      }
      const name = JSON.parse(body).name;
      console.log(name);
    });
  }); 
  });
}

f1();