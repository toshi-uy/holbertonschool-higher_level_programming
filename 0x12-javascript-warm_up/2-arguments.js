#!/usr/bin/node
const argv = process.argv.length;

if (argv === 2) {
  console.log('No argument');
} else if (argv === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
