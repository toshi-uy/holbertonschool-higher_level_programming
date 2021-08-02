#!/usr/bin/node
const argv = process.argv[2];
function factorial(num) {
  if (num < 0) {
      throw new Error("num must not be negative");
  }
  return num <= 1 ? 1 : num * factorial(num - 1);
}

let result = factorial(argv);
console.log(result);
