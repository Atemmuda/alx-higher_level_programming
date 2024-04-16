#!/usr/bin/node

8
/**
 * converter - converts from one base to the other
 * @param {*} base:- initial base of the given numbers
 * @returns - new numbers in the converted form
 */

exports.converter = function (base) {
  return function innerFunction (inner) {
    return parseInt(inner).toString(base);
  };
};
