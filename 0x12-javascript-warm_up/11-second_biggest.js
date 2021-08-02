#!/usr/bin/node
const argv = process.argv;

if (argv.length === 2) {
  console.log(0);
} else if (argv.length === 3) {
  console.log(0);
} else {
  let max = argv[0];
  for (let i = 2; i < argv.length - 1; i++) {
    if (argv[i] >= max) {
      max = argv[i];
    }
  }
  console.log(max);
}
