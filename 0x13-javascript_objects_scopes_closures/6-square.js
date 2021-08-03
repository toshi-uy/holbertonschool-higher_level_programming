#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        process.stdout.write(c);
      }
      console.log('');
    }
  }
}
