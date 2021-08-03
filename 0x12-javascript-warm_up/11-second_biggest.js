#!/usr/bin/node
const argv = process.argv;
if (argv.length === 2) {
  console.log(0);
} else if (argv.length === 3) {
  console.log(0);
} else {
  process.argv.sort((a, b) => a - b);
  console.log(process.argv[process.argv.length - 2]);
}
