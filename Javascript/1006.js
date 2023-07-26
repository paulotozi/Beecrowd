const prompt = require("prompt-sync")();

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var n1 = parseFloat(prompt());
var n2 = parseFloat(prompt());
var n3 = parseFloat(prompt());

console.log("MEDIA = %s", ((n1 * 0.2) + (n2 * 0.3) + (n3 * 0.5)).toFixed(1));

//solucao do beecrowd
/*var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var n1 = parseFloat(lines.shift());
var n2 = parseFloat(lines.shift());
var n3 = parseFloat(lines.shift());

console.log("MEDIA = %s", ((n1 * 0.2) + (n2 * 0.3) + (n3 * 0.5)).toFixed(1));*/