#!/usr/bin/node
function resolveAfter2Seconds(x) {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve(x);
    }, 2000);
  });
}

function f2() {
  const filmNbr = process.argv[2];
  const request = require('request');
  const url = 'https://swapi-api.hbtn.io/api/films/' + filmNbr;
  request(url, function (error, response, body) {
    if (error) {
      console.error(error);
    }
    const path = JSON.parse(body).characters;
    return path;
  }
,

async function f1(path) {
  const x = await resolveAfter2Seconds(10);
  path = f2()
  path.forEach(element => {
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