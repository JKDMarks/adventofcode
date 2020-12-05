const wires = require('./input.json');
const [wire1, wire2] = wires;

// const findDims = (wire) => {
// 	let [height, width] = [0, 0];
// 	let [maxU, maxD, maxR, maxL] = [0, 0, 0, 0];
// 	wire.forEach((mvmt) => {
// 		const dir = mvmt[0];
// 		const dist = Number(mvmt.slice(1));
// 		if (dir === 'U') {
// 			height += dist;
// 			maxU = Math.max(maxU, height);
// 		} else if (dir === 'D') {
// 			height -= dist;
// 			maxD = Math.min(maxD, height);
// 		} else if (dir === 'R') {
// 			width += dist;
// 			maxR = Math.max(maxR, width);
// 		} else if (dir === 'L') {
// 			width -= dist;
// 			maxL = Math.min(maxL, width);
// 		}
// 	});
// 	console.log(maxU, maxD, maxR, maxL);
// 	return [height, width];
// };

const traceWires = () => {
	const visited1 = {
		// '0,0': true,
		// '0,1': true,
	};
	const intersections = [];
	let currPos = [0, 0];

	const move = (mvmt, wireNum) => {
		const dir = mvmt[0];
		const dist = Number(mvmt.slice(1));
		for (let i = 0; i < dist; i++) {
			if (dir === 'U') {
				currPos[1]++;
			} else if (dir === 'D') {
				currPos[1]--;
			} else if (dir === 'R') {
				currPos[0]++;
			} else if (dir === 'L') {
				currPos[0]--;
			}

			const posStr = currPos.join(',');
			if (wireNum === 1) {
				visited1[posStr] = true;
			} else if (wireNum === 2 && posStr in visited1) {
				intersections.push([...currPos]);
			}
		}
	};

	wire1.forEach((mvmt) => move(mvmt, 1));
	currPos = [0, 0];
	wire2.forEach((mvmt) => move(mvmt, 2));

	console.log('intersections', intersections);

	let closest = Number.MAX_SAFE_INTEGER;
	intersections.forEach((intArr) => {
		const dist = Math.abs(intArr[0]) + Math.abs(intArr[1]);
		closest = Math.min(closest, dist);
	});
	console.log('closest', closest);

	return intersections;
};

// traceWires();

const findClosestIntersection = () => {
	const intersections1 = traceWires().reduce(
		(acc, cur) => ({ ...acc, [cur.join(',')]: true }),
		{}
	);
	const intersections2 = { ...intersections1 };

	let moveCt = 0;
	let currPos = [0, 0];
	const move = (mvmt, wireNum) => {
		const dir = mvmt[0];
		const dist = Number(mvmt.slice(1));
		for (let i = 0; i < dist; i++) {
			moveCt++;
			if (dir === 'U') {
				currPos[1]++;
			} else if (dir === 'D') {
				currPos[1]--;
			} else if (dir === 'R') {
				currPos[0]++;
			} else if (dir === 'L') {
				currPos[0]--;
			}

			const posStr = currPos.join(',');
			if (wireNum === 1 && intersections1[posStr] === true) {
				intersections1[posStr] = moveCt;
			} else if (wireNum === 2 && intersections2[posStr] === true) {
				intersections2[posStr] = moveCt;
			}
		}
	};

	wire1.forEach((mvmt) => move(mvmt, 1));
	currPos = [0, 0];
	moveCt = 0;
	wire2.forEach((mvmt) => move(mvmt, 2));

	const intersectionsSum = {};
	Object.entries(intersections1).forEach(([k, v]) => (intersectionsSum[k] = v));
	Object.entries(intersections2).forEach(([k, v]) => (intersectionsSum[k] += v));

	return Math.min(...Object.values(intersectionsSum));
};

console.log(findClosestIntersection());
