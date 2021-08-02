#!/usr/bin/node
let size = parseInt(process.argv[2]);
let i, j;
if (size === undefined || isNaN(size)) {
  console.log('Missing size');
}
if (size > 0) {
  for (i = 0; i < size; i++) {
    for (j = 0; j < size; j++) {
      print('X');
    }
    println('');
  }
}
