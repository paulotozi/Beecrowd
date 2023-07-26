const prompt = require("prompt-sync")();

var n1 = parseInt(prompt());
var n2 = parseInt(prompt());
var n3 = parseFloat(prompt());

console.log("NUMBER = %s",n1);
console.log("SALARY = U$ %s", (n2 * n3).toFixed(2));

//solucao do beecrowd
/*var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var n1 = parseInt(lines.shift());
var n2 = parseInt(lines.shift());
var n3 = parseFloat(lines.shift());

console.log("NUMBER = %s",n1);
console.log("SALARY = U$ %s", (n2 * n3).toFixed(2));*/