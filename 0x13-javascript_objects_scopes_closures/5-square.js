#!/usr/bin/node
import { Rectangle } from '4-rectangle';

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
