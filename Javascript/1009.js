const prompt = require("prompt-sync")();

var name = prompt();
var salary = parseFloat(prompt());
var sales = parseFloat(prompt());

console.log("TOTAL = R$ %s", (salary + (sales * 0.15)).toFixed(2));

//solucao do beecrowd
/*var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var name = lines.shift();
var salary = parseFloat(lines.shift());
var sales = parseFloat(lines.shift());

console.log("TOTAL = R$ %s", (salary + (sales * 0.15)).toFixed(2));*/