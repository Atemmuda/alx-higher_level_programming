#!/usr/bin/node

/**
 * esrever - function that reverses an array parameter
 * @param {*} list array of elements
 * @returns new array in reverse order
 */
exports.esrever = function (list) {
  const result = [];
  for (let i = list.length - 1; i >= 0; i--) {
    result.push(list[i]);
  }
  return result;
};
