#!/usr/bin/node

exports.esrever = function (list) {
  let j = list.length - 1;
  let i = 0;
  for (i, j; i >= j; i++, j--) {
    const temp = list[i];
    list[i] = list[j];
    list[j] = temp;
  }
  return (list);
};
