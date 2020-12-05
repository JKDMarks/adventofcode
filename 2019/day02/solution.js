const input = require('./input.json');

const runProgram = (p1, p2) => {
	const arr = [input[0], p1, p2, ...input.slice(3)];
	const handle1 = (a, b, c) => (arr[c] = arr[a] + arr[b]);
	const handle2 = (a, b, c) => (arr[c] = arr[a] * arr[b]);

	for (let i = 0; i < arr.length; i++) {
		const [curr, a, b, c] = arr.slice(i, i + 4);
		if (curr === 1) {
			handle1(a, b, c);
		} else if (curr === 2) {
			handle2(a, b, c);
		} else if (curr === 99) {
			break;
		}
		i += 3;
	}
	return arr[0];
};

console.log(runProgram(12, 2)); // 3850704

const target = 19690720;

for (let x = 0; x <= 100; x++) {
	for (let y = 0; y <= 100; y++) {
		const output = runProgram(x, y);
		const pct = output / target;
		// if (pct >= 0.95 && pct <= 1.05) {
		// 	console.log(x, y, output, output / target);
		// }
		if (output === target) {
			console.log(x, y, output); // 67 18 19690720
			console.log(100 * x + y);
		}
	}
}
