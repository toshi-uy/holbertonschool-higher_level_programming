#!/usr/bin/node
const url = process.argv[1];
const options = {
  uri: url
}
request(options, function (response) {
  console.log('Code:', response.statusCode); 
});
