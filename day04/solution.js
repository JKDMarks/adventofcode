const arr = require('./input.json');

const validateNumber = (numStr, lb, ub) => {
	const num = Number(numStr);
	return Number.isInteger(num) ? (lb <= num && num <= ub) : false;
};

const validation = {
	byr: byr => validateNumber(byr, 1920, 2002),
	iyr: iyr => validateNumber(iyr, 2010, 2020),
	eyr: eyr => validateNumber(eyr, 2020, 2030),
	hgt: hgt => {
		const last2 = hgt.slice(-2);
		const height = Number(hgt.slice(0, -2));

		if (last2 === 'cm') {
			return validateNumber(height, 150, 193);
		} else if (last2 === 'in') {
			return validateNumber(height, 59, 76);
		} else {
			return false;
		}
 	},
	hcl: hcl => /^#[0-9a-f]{6}$/.test(hcl),
	ecl: ecl =>['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].includes(ecl),
	pid: pid => /^\d{9}$/.test(pid),
	cid: () => true,
};

const isValid = pp => {
	const keys = Object.keys(pp);
	if (keys.length < 7) {
		return false;
	} else if (keys.length === 7 && keys.includes('cid')) {
		return false;
	} else {
		return true;
	}
};

const validOnly = arr.filter(isValid);

console.log(validOnly.length);

const trueValid = validOnly.filter(pp => {
	for (const key in pp) {
		const val = pp[key];
		if (validation[key](val)) {
			continue;
		} else {
			return false;
		}
	}
	return true;
});

console.log(trueValid.length);