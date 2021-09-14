#!/usr/bin/node
const argv1 = process.argv[2];
const argv2 = process.argv[3];
const fs = require('fs');
fs.appendFile(argv2, argv1, function (err) {
  if (err) throw err;
});
