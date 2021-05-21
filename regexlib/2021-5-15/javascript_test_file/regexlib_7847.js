/* 7847
 * [0-9]*\.?[0-9]*[1-9]
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"0"*1024+"◎@! _1SLQ_1"
 */
var REGEX = /[0-9]*\.?[0-9]*[1-9]/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '0'.repeat(i*1) + '◎@! _1SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}