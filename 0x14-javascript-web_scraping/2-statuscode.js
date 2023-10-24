#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.error('error:', err);
  } else {
    console.log('code:', res && res.statusCode);
  }
});
