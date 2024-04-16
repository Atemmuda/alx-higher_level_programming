#!/usr/bin/node

const BaseSquare = require('./5-square');

/**
 * Square - basic square inherited from Rectangle
 * @size : size of square
 *
 * Return
 */
class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let row = 0; row < this.height; row++) {
        for (let column = 0; column < this.width; column++) {
          process.stdout.write('C');
        }
        process.stdout.write('\n');
      }
    }
  }
}

module.exports = Square;
