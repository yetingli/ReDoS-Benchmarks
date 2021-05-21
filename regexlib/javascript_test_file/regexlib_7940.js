/* 7940
 * Last.*?(\d+.?\d*)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"Last"+"1"*1024+"! _1SLQ_2"
 */
var REGEX = /Last.*?(\d+.?\d*)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'Last' + '1'.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}