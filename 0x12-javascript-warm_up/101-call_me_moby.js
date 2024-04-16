#!/usr/bin/node

// The function must be visible from outside
exports.callMeMoby = function (x, theFunction) {
  for (let i = 1; i <= x; i++) {
    theFunction();
  }
};
