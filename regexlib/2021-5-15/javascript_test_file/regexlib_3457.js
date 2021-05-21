/* 3457
 * ([0-9]+)\s(d)\s(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"0"*10000+"!_1SLQ_1"
 */
var REGEX = /([0-9]+)\s(d)\s(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '0'.repeat(i*10000) + '!_1SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}