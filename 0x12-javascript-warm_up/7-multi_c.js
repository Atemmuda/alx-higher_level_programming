#!/usr/bin/node

const parameter = process.argv[2];

/**
 * Where x is the first argument of the script
 * If the first argument can’t be converted to an integer,
 * print “Missing number of occurrences”
 */

if (isNaN(parseInt(parameter))) {
  console.log('Missing number of occurrences');
} else if (parameter < 0) {
  process.exit();
} else {
  let i = 0;
  while (i < parameter) {
    console.log('C is fun');
    i++;
  }
}
