#!/usr/bin/node

exports.esrever = function (list) {
  newList = [];
  let i = list.length - 1;
  for (i; i >= 0; i--) {
    newList.push(list[i]);
  }
  return (newList);
};
