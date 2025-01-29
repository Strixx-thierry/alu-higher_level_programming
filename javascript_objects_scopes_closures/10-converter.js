#!/usr/bin/node
<<<<<<< HEAD
let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
=======
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
>>>>>>> b7d79a6874a66683d2dfdae9818c1ef80dcfa248
