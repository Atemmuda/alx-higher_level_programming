#!/usr/bin/node

const consoleArg2 = process.argv[2];
const consoleArg3 = process.argv[3];

/**
 * Add two integers passed from the console
 *
 * @param {*} a first argument
 * @param {*} b second argument
 * @returns sum of 'a' and 'b'
 */
function add (a, b) {
  return (a + b);
}

console.log(add(parseInt(consoleArg2), parseInt(consoleArg3)));
