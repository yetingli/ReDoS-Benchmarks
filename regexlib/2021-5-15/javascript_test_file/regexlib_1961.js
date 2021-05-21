/* 1961
 * [_\w-]+(?:\.[_\w-]+)*@(?:[\w-]+\.)+(?:[\w-]{2,4})(?![\w]+)
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"_"*10000+"◎@! _1SLQ_1"
 */
var REGEX = /[_\w-]+(?:\.[_\w-]+)*@(?:[\w-]+\.)+(?:[\w-]{2,4})(?![\w]+)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '_'.repeat(i*10000) + '◎@! _1SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}