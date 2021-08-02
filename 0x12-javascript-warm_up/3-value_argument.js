#!/usr/bin/node
const argv = process.argv[2];
if (!argv) {
  console.log('No argument');
} else {
  console.log(argv);
}
