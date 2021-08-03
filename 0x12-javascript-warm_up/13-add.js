#!/usr/bin/node
function add (a,b) {
  return (a + b);
}

const _add = add;
export { _add as add };
