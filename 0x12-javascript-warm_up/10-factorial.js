#!/usr/bin/node
const num = parseInt(process.argv[2]);
function factorial(x) {
  if (x === 0) {
      return 1;
  }
  else {
      return x * factorial(x - 1);
  }
}
if (isNaN(num)) {
  console.log(1);
}
if (num > 0 && isNaN(num) === false) {
  console.log(factorial(num));
}
