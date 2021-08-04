#!/usr/bin/node

const list = require('./100-map.js');
let newList = list.map(x, index => x * index);
return (newList);
