#!/usr/bin/node

const { list } = require('./100-data');

const result = list.map((element, index) => element * index);

console.log(list);
console.log(result);
