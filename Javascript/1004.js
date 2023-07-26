const prompt = require("prompt-sync")();

var n1 = parseInt(prompt());
var n2 = parseInt(prompt());

console.log("PROD = %s", n1 * n2);

//solucao do beecrowd
/*var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var n1 = parseInt(lines.shift());
var n2 = parseInt(lines.shift());

console.log("PROD = %s", n1 * n2);*/