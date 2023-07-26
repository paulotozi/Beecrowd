const prompt = require("prompt-sync")();

var n1 = parseFloat(prompt());
var n2 = parseFloat(prompt());

console.log("MEDIA = %s", (((n1 * 3.5) + (n2 * 7.5)) / 11).toFixed(5));

//solucao do beecrowd
/*var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var n1 = parseFloat(lines.shift());
var n2 = parseFloat(lines.shift());

console.log("MEDIA = %s", (((n1 * 3.5) + (n2 * 7.5)) / 11).toFixed(5));*/