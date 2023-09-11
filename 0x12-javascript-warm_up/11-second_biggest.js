#!/usr/bin/node
const arg = process.argv.slice(2).map(Number);
if (arg.length <= 1) {
  console.log(0);
} else {
  arg.sort((a, b) => b - a);
  console.log(arg[1]);
}
