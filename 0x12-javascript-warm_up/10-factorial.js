#!/usr/bin/node
const num = process.argv[2];
function factorial(x) {
  if (x === 0) {
      return 1;
  }
  else {
      return x * factorial(x - 1);
  }
}

if (num > 0) {
  let result = factorial(3);
  console.log(result);
}
