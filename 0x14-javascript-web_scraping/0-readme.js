#!/usr/bin/node
const argv = process.argv[2];
const fs = require('fs');
try {
  const data = fs.readFileSync(argv, 'utf8');
  console.log(data.toString());    
} catch (e) {
  console.log('Error:', e);
}
