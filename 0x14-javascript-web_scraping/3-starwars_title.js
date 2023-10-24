#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (err, res, body) {
  if (err) {
    console.error('error:', err);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
