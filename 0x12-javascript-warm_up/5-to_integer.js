#!/usr/bin/node
const arg = process.argv.slice(2);
const num = Number(arg[0]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Math.floor(num));
}
