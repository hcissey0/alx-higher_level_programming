#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.error('error:', err);
  } else {
    const todos = JSON.parse(body);
    const completedtasks = {};
    todos.forEach((task) => {
      if (task.completed) {
        if (completedtasks[task.userId]) {
          completedtasks[task.userId]++;
        } else {
          completedtasks[task.userId] = 1;
        }
      }
    });
    console.log(completedtasks);
  }
});
