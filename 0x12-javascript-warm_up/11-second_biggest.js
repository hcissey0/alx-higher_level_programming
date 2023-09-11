#!/usr/bin/node
let sb = 0;
let b = 0;
const arg = process.argv.slice(2);
for (let i = 0; i < arg.length; i++) {
  if (Number(arg[i]) > b) {
    sb = b;
    b = Number(arg[i]);
  }
}
console.log(sb);
