#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, function (err, res, body) {
  if (err) {
    console.error('error:', err);
  } else {
    const film = JSON.parse(body);
    const urls = film.characters;
    const proms = urls.map((ur) => getName(ur));
    Promise.all(proms).then((names) => names.forEach((name) => console.log(name)));
  }
});

function getName (url) {
  return new Promise((resolve, reject) => {
    request(url, function (err, resp, body) {
      if (err) {
        reject(err);
      } else {
        const cha = JSON.parse(body);
        resolve(cha.name);
      }
    });
  });
}
