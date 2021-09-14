#!/usr/bin/node
const argv1 = process.argv[2];
const argv2 = process.argv[3];
const req = require('request');
try {
  const data = request.get(argv1, 'utf8');
  const fs = require('fs');
  fs.appendFile(data, argv2, function (err) {
    if (err) throw err;
  });
} catch (e) {
  console.log('Error:', e);
}
