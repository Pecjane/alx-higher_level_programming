#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  /**
     * function that returns number of occurrences in a list.
     */
  let occur = 0;

  for (const elem in list) {
    if (list[elem] === searchElement) {
      occur += 1;
    }
  }
  return occur;
};
