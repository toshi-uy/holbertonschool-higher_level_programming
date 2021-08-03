#!/usr/bin/node
const argv = process.argv;
if (argv.length === 2) {
  console.log(0);
} else if (argv.length === 3) {
  console.log(0);
} else {
  let secondMax = argv[2];
  argv.sort();
  for (let i = 2; i < argv.length - 1; i++) {
    if (argv[i] > argv[i + 1]) {
      secondMax = argv[i];
    }
  }
  console.log(secondMax);
}
