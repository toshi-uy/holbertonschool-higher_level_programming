#!/usr/bin/node

exports.esrever = function (list) {
  newList = [];
  let j = list.length - 1;
  for (i; i >= 0; i--) {
    newList.push(list[i]);
  }
  return (list);
};
