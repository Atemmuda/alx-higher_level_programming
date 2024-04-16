#!/usr/bin/node

// a function that prints the number of arguments already printed and the new argument value.

let elementNumber = 0;
exports.logMe = function (item) {
  const printing = elementNumber + ': ' + item;
  console.log(printing);
  elementNumber++;
};
