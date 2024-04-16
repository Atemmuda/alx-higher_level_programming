#!/usr/bin/node

/**
 * nbOccurences - function that count the number of occurence of
 * element in a list
 * @param {*} list-: array
 * @param {*} searchElement-: elements to look up for in array of list
 * @returns - number of occurences of searchElement
 */
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let i = 0; i <= list.length - 1; i++) {
    if (list[i] === searchElement) {
      counter++;
    }
  }
  return counter;
};
