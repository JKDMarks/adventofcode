const fs = require('fs');
const input = fs.readFileSync('./raw-input.txt', 'utf8');

const [wire1, wire2] = input.split('\n').map((wire) => wire.split(','));

fs.writeFileSync('./input.json', JSON.stringify([wire1, wire2]));
