/* 8003
 * (AUX|PRN|NUL|COM\d|LPT\d)+\s*$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"AUX"*5000+"!_1SLQ_1"
 */
var REGEX = /(AUX|PRN|NUL|COM\d|LPT\d)+\s*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'AUX'.repeat(i*10000) + '!_1SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}