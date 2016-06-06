#!/usr/bin/env node
const fs = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(runTest);

function runTest(line) {
  console.log(line.replace(/(.)\1+/g, "$1"))
}
