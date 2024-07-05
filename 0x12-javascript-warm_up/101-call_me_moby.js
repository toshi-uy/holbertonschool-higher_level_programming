#!/usr/bin/node
function callMeMoby(times, func) {
  for (let i = 0; i < times ; i++) {
    func();
  }
}

module.exports = {
    callMeMoby: callMeMoby
};
