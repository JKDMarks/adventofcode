const arr = require('./input.json');

const calcFuel = (mass) => {
	const possibleFuel = Math.floor(mass / 3) - 2;
	return possibleFuel >= 0 ? possibleFuel : 0;
};

const totalFuel = arr.reduce((acc, cur) => acc + calcFuel(cur), 0);

console.log(totalFuel);

const totalFuel2 = arr.reduce((acc, cur) => {
	let currFuel = calcFuel(cur);
	let total = currFuel;
	while (currFuel > 0) {
		currFuel = calcFuel(currFuel);
		total += currFuel;
	}
	return acc + total;
}, 0);

console.log(totalFuel2);
