const arr = require('./input.json');

const splitStr = str => {
	const [pattern, pw] = str.split(': ');
	const [nums, ltr] = pattern.split(' ');
	const [n1, n2] = nums.split('-').map(s => Number(s));
	return [n1, n2, ltr, pw];
};

const findValidCount = arr => {
	let validCount = 0;
	arr.forEach(str => {
		const [lb, ub, ltr, pw] = splitStr(str);
		const rgx = new RegExp(ltr, 'g');

		const match = pw.match(rgx);
		if (match !== null) {
			const ct = match.length;
			if (lb <= ct && ct <= ub) {
				validCount++;
			}
		}
	});
	return validCount;
};

const findValidCount2 = arr => {
	let validCount = 0;
	arr.forEach(str => {
		const [fp, sp, ltr, pw] = splitStr(str);
		const toCheck = pw[fp-1] + pw[sp-1];
		const rgx = new RegExp(ltr, 'g');

		const match = toCheck.match(rgx);
		if (match && match.length === 1) {
			validCount++;
		}
	});
	return validCount;
}

console.log(findValidCount(arr));
console.log(findValidCount2(arr));