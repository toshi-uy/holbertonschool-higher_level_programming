#!/usr/bin/node
const url = process.argv[2];
const options = {
  uri: url
}
request(options, function (response) {
  console.log('Code:', response.statusCode); 
});
