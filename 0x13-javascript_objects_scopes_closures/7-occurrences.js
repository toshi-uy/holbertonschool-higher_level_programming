#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let ocurrency = 0;
    list.forEach(searchElement => {
        ocurrency += 1;
        return ocurrency;
    });
}
