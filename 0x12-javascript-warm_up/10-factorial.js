#!/usr/bin/node
const num = process.argv[2];
function factorial(x) {
  if (x < 0) {
    console.log("num must not be negative");
  }
  if (x <= 1) {
    return 1;
  }
  return x * factorial(x - 1);
}

let result = factorial(3);
console.log(result);
