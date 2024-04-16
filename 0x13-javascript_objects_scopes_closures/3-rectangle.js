#!/usr/bin/node

/**
 * Rectangle - basic rectangle representation
 * @width : width of rectangle
 * @height : height of the rectangle
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      for (let column = 0; column < this.width; column++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
}

module.exports = Rectangle;
