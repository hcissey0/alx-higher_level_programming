#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.error('error:', err);
  } else {
    const films = JSON.parse(body);
    let c = 0;
    films.results.forEach((film) => {
      film.characters.forEach((cha) => {
        if (cha.includes('18')) {
          c++;
        }
      });
    });
    console.log(c);
  }
});
