#!/usr/bin/node

const consoleArg2 = process.argv[2];

/**
 * finds the factorial of a number
 * The first argument is integer (argument can be cast as integer)
 * used for computing the factorial
 * Factorial of NaN is 1
 * do it recursively
 * @param {*} n number to compute its factorial
 * @returns factorial of a given number
 */

function factorial (n) {
  const result = 1;
  if (n === 0 || isNaN(n)) {
    return result;
  }
  return factorial(n - 1) * n;
}

// console printer with given console input
console.log(factorial(consoleArg2));
