#!/usr/bin/node

exports.esrever = function (list) {
  let j = list.length - 1;
  for (let i = 0, j; i >= j; i++, j--) {
    const temp = list[i];
    list[i] = list[j];
    list[j] = temp;
  }
  return (list);
};
