#!/usr/bin/node
const dict_pec = require('./101-data.js').dict;
const newDict_pec = {};
for (const key5 in dict_pec) {
  if (newDict_pec[dict[key5]] === undefined) {
    newDict_pec[dict[key5]] = [key5];
  } else {
    newDict_pec[dict[key5]].push(key5);
  }
}
console.log(newDict_pec);
