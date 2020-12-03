const arr = require('./input.json');
const width = arr[0].length;
const height = arr.length;

const check = (posArr) => {
	const row = arr[posArr[0]];
	return row ? row[posArr[1]] : null;
};

const go = (currPosArr, y, x) => {
	return [currPosArr[0] + y, (currPosArr[1] + x) % width];
};

const countTrees = (y, x) => {
	let currPos = [0, 0]; // [y, x]
	let crashCount = 0;
	while (currPos[0] <= height) {
		if (check(currPos) === '#') {
			crashCount++;
		}
		currPos = go(currPos, y, x);
	}
	return crashCount;
};

console.log(countTrees(1, 1));
console.log(countTrees(1, 3));
console.log(countTrees(1, 5));
console.log(countTrees(1, 7));
console.log(countTrees(2, 1));