#!/usr/bin/node
exports.addMeMaybe = function (num, func) {
  num++;
  func(num);
};
