#!/usr/bin/node

const Rectangle = require('./4-rectangle');

/**
 * Square - basic rectangle representation
 * @width : width of rectangle
 * @height : height of the rectangle
 *
 * Return
 */
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
