#!/usr/bin/node

/**
 * You can assume all arguments can be converted to integer
 * If no argument passed, print 0
 * If the number of arguments is 1, print 0
 */
let biggest = 0;
let secondBiggest = 0;

for (let index = 2; index < process.argv.length; index++) {
  const number = parseInt(process.argv[index]);

  if (biggest < number) {
    secondBiggest = biggest;
    biggest = number;
  } else if (secondBiggest < number) {
    secondBiggest = number;
  }
}

console.log(secondBiggest);
