#!/usr/bin/node
let size = parseInt(process.argv[2]);
if (size === undefined || isNaN(size)) {
  console.log('Missing size');
}
if (size > 0) {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      console.log("X");
    }
    console.log("");
  }
}
