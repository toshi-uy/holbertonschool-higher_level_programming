#!/usr/bin/node
const file = require('fs');
const first = file.readFileSync(process.argv[2]);
const second = file.readFileSync(process.argv[3]);
file.writeFileSync(process.argv[4], first + second);
