function addMeMaybe (number, func) {
  number++;
  func(number);
}

module.exports.addMeMaybe = addMeMaybe;
