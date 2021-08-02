#!/usr/bin/node
import argv from 'process';
const argv = require('process');

if (argv[1]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
