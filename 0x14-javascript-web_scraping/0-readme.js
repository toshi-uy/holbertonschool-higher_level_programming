#!/usr/bin/node
const argv = process.argv[2];
var fs = require('fs');
try {  
    var data = fs.readFileSync(argv, 'utf8');
    console.log(data.toString());    
} catch(e) {
    console.log('Error:', e);
}
