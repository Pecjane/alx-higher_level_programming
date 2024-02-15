#!/usr/bin/node
let sample = 0;
exports.logMe = function (item) { console.log(`${sample++}: ${item}`); };
