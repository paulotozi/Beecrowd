const prompt = require("prompt-sync")();

var a = parseInt(prompt());
var b = parseInt(prompt());
var c = parseInt(prompt());
var d = parseInt(prompt());

console.log("DIFERENCA = %s", (a * b) - (c * d));

//solucao do beecrowd
/*var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var a = parseInt(lines.shift());
var b = parseInt(lines.shift());
var c = parseInt(lines.shift());
var d = parseInt(lines.shift());

console.log("DIFERENCA = %s", (a * b) - (c * d));*/