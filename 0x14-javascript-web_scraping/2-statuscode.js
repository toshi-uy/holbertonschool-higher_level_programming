#!/usr/bin/node
const url = process.argv[2];
request(url)
.on('response', function(response) {
    console.log("Code:",response.statusCode)
});
