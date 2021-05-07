/**
 * vuln pattern: SLQ
 * vuln degree: POL
 * mul vuln: N
 * vuln location: 0-1
 */
var REGEX = /.*(?=tt\d)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'a'.repeat(i*10000) + '!'
    REGEX.exec(attack_str);
    var time_cost = Date.now() - time;
    console.log("i.length: " + i + ": " + time_cost+" ms")
}