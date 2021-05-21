/* 3640
 * (\/\*(\s*|.*?)*\*\/)|(--.*)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"/*"+"\r\t"*8+"◎@! _1!\n_SLQ_3"
 */
var REGEX = new RegExp("(\/\*(\s*|.*?)*\*\/)|(--.*)")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '/*' + '\r\t'.repeat(i*1) + '◎@! _1!\n_SLQ_3'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}