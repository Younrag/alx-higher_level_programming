#!/usr/bin/node

const { argv } = require('node:process');
const no = 'No argument';
const yes = 'Arguments found';
let count = 0;
// print process.argv
argv.forEach((val, index) => {
  count++;
});
if (count === 2) {
  console.log(no);
} else if (count >= 3) {
  console.log(yes);
}
