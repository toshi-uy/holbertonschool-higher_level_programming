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
else if (num > 0) {
  console.log(factorial(num));
}
