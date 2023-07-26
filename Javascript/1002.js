const prompt = require("prompt-sync")();

var R = prompt();
//(lines.shift());
var A = 3.14159 * (R ** 2);

console.log("A=%s",A.toFixed(4));

//solucao do beecrowd
/*var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var R = (lines.shift());
var A = 3.14159 * (R ** 2);

console.log("A=%s",A.toFixed(4));*/