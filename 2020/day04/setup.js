const fs = require('fs');

const input = fs.readFileSync('./raw-input.txt', 'utf8');

const arr = input.split('\n\n').map((str) => {
	const pairs = str.replace(/\n/g, ' ').split(' ');
	const obj = {};
	pairs.forEach((pair) => {
		const [key, val] = pair.split(':');
		obj[key] = val;
	});
	return obj;
});

fs.writeFileSync('./input.json', JSON.stringify(arr));
