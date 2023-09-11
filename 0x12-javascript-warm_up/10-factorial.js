#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }
  return factorial(num - 1) * num;
}

console.log(factorial(Number(process.argv[2])));
