const arr = require("./input.json");

// const getProduct = (arr, indices) => {
// 	return indices.reduce((acc, cur) => {
// 		return acc * arr[cur];
// 	}, 1);
// };

const findPair = (arr, tgt) => {
  const tracker = {};
  const pair = [];
  arr.forEach((num, i) => {
    const diff = tgt - num;
    if (diff in tracker) {
      pair.push(num, diff);
    }
    tracker[num] = i;
  });
  return pair.length ? pair : null;
};

const set1 = findPair(arr, 2020);

let set2 = [];
arr.forEach((num, i) => {
  const pair = findPair(arr.slice(i), 2020 - num);
  if (pair) {
    set2 = set2.concat(num).concat(pair);
  }
});

console.log(set1, set1[0] * set1[1]);
console.log(set2, set2[0] * set2[1] * set2[2]);
