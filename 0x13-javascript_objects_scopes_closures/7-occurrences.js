#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let ocurrency = 0;
    list.forEach(element => {
        if (element === searchElement) {
            ocurrency += 1;
        }
    });
    return ocurrency;
}
