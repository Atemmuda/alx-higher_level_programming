#!/usr/bin/node

const consoleArg = process.argv[2];

/**
 * The first argument is the size of the square
 * If the first argument can’t be converted to an integer, print “Missing size”
 * You must use the character X to print the square
 */

if (isNaN(parseInt(consoleArg))) {
  console.log('Missing size');
} else if (consoleArg < 0) {
  process.exit();
} else {
  let i = 0;
  let j = 0;
  let append = '';
  while (j < consoleArg) {
    append += 'X';
    j++;
  }
  while (i < consoleArg) {
    console.log(append);
    i++;
  }
}
