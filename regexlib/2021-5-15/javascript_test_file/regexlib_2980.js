/* 2980
 * (\s+|)((\(\d{3}\) +)|(\d{3}-)|(\d{3} +))?\d{3}(-| +)\d{4}( +x\d{1,4})?(\s+|)
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+" "*5000+"!_1◎@! _1SLQ_1"
 */
var REGEX = /(\s+|)((\(\d{3}\) +)|(\d{3}-)|(\d{3} +))?\d{3}(-| +)\d{4}( +x\d{1,4})?(\s+|)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + ' '.repeat(i*10000) + '!_1◎@! _1SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}