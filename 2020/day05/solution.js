const input = require('./input.json');

const plane = [];
for (let i = 0; i <= 127; i++) {
	plane[i] = [0, 0, 0, 0, 0, 0, 0, 0];
}

const getSeatId = ([row, col]) => row * 8 + col;

const parseRowOrCol = (range, rowOrColStr) => {
	rowOrColStr.split('').forEach((ltr) => {
		const [a, b] = range;
		const amtToChange = Math.round((b - a) / 2);
		if (ltr === 'F' || ltr === 'L') {
			range[1] -= amtToChange;
		} else if (ltr === 'B' || ltr === 'R') {
			range[0] += amtToChange;
		}
	});
};

const findSeat = (seat) => {
	const rowStr = seat.slice(0, 7);
	const colStr = seat.slice(7);
	let rowRange = [0, 127];
	let colRange = [0, 7];

	parseRowOrCol(rowRange, rowStr);
	parseRowOrCol(colRange, colStr);

	return [rowRange[0], colRange[0]];
};

// console.log(getSeatId(findSeat('BFFFBBFRRR'))); // 70, 7, 567
// console.log(getSeatId(findSeat('FFFBBBFRRR'))); // 14, 7, 119
// console.log(getSeatId(findSeat('BBFFBBFRLL'))); // 102, 4, 820

const takenSeatIds = {};

let highestId = Number.MIN_SAFE_INTEGER;
input.forEach((seatStr) => {
	const seatId = getSeatId(findSeat(seatStr));
	takenSeatIds[seatId] = true;
	highestId = Math.max(highestId, seatId);
});

console.log(highestId);

for (let i = 36; i <= 944; i++) {
	const iStr = i.toString();
	if (!(iStr in takenSeatIds)) {
		console.log(iStr);
	}
}
