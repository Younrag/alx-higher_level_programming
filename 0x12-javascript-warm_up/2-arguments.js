#!/usr/bin/node

const process = require('process');
const no = 'No argument';
const yes = 'Argument found';
const yes2 = 'Arguments found';
// print process.argv
if (process.argv.length === 2) {
  console.log(no);
} else if (process.argv.length === 3) {
  console.log(yes);
} else {
  console.log(yes2);
}
