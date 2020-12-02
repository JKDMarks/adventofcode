const fs = require('fs');

const args = process.argv.slice(2);
const [url, dir] = args;

axios.get(url).then(resp => {
	console.log(resp)
});