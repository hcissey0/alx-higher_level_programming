#!/usr/bin/node
const dict = require('./101-data.js').dict;
const ndict = {};
for (const key in dict) {
  if (ndict[dict[key]]) {
    ndict[dict[key]].push(key);
  } else {
    ndict[dict[key]] = [key];
  }
}
console.log(ndict);
