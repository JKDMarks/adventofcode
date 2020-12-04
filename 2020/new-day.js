const fs = require('fs');
const args = process.argv.slice(2);
const day = args[0];

const setup = `const fs = require('fs');

const input = fs.readFileSync('./raw-input.txt', 'utf8');

const arr = input.split('\\n');

fs.writeFileSync('./input.json', JSON.stringify(arr));`;

const solution = `const arr = require('./input.json');`;

fs.mkdirSync(day);
fs.writeFileSync(`./${day}/setup.js`, setup);
fs.writeFileSync(`./${day}/solution.js`, solution);
fs.writeFileSync(`./${day}/raw-input.txt`, '');
fs.writeFileSync(`./${day}/input.json`, '');
