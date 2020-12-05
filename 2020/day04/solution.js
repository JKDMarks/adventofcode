const arr = require('./input.json');

const validation = {
	byr: (byr) => /^(19[2-9]\d|200[0-2])$/.test(byr),
	iyr: (iyr) => /^20(1\d|20)$/.test(iyr),
	eyr: (eyr) => /^20(2\d|30)$/.test(eyr),
	hgt: (hgt) => /^(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)$/.test(hgt),
	hcl: (hcl) => /^#[0-9a-f]{6}$/.test(hcl),
	ecl: (ecl) => ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].includes(ecl),
	pid: (pid) => /^\d{9}$/.test(pid),
	cid: () => true,
};

const isValid = (pp) => {
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

console.log(validOnly.length); // 222

const trueValid = validOnly.filter((pp) =>
	Object.entries(pp).every(([key, val]) => validation[key](val))
);

console.log(trueValid.length); // 140
