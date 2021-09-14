#!/usr/bin/node
const url = process.argv[2];
const fs = require('fs');
fs.GET(url, (err, res) => {
  if (err) return console.log('Error: ', err);
  console.log("Code: %d", res.statusCode);
});
