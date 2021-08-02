#!/usr/bin/node
const myVar = 'C is fun';
const argv = process.argv[2];
if (argv === undefined) {
  console.log('Missing number of occurrences')
}
if(argv >= 0) {
  while (argv >= 0) {
    console.log(myVar);
    argv--;
  }
}
