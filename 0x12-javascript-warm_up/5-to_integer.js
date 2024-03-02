#!/usr/bin/node

/*
<<<<<<< HEAD
 * prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer
 * else prints "Not a number".
 */
=======
 *  * prints My number: <first argument converted in integer>
 *   * if the first argument can be converted to an integer
 *    * else prints "Not a number".
 *     */
>>>>>>> 7c1cc99d4e492f3bf8f317dbf9b58f12992621f1

const arg = process.argv[2];

if (isNaN(parseInt(arg))) {
	  console.log('Not a number');
} else {
	  console.log('My number:', parseInt(arg));

}
