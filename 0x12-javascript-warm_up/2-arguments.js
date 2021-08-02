#!/usr/bin/node
import argv from 'process';
const argv = process.argv;
if (argv[1]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
