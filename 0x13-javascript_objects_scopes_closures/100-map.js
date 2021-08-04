#!/usr/bin/node

const list = require('./100-map.js');
console.log(list);
let newList = list.map(function(x, index) {x * index});
console.log(newList);
