#!/usr/bin/node
exports.callmemoby = function (x, thefunction) {
	for (let i = 0; i < x; i++) {
		theFunction();
	}
};
