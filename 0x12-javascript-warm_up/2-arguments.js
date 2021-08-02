#!/usr/bin/node
const argv = require('process');

if (argv[0]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
