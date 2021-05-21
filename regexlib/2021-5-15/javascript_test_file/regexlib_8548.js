/* 8548
 * (?:\b\w*(\w\w?)\1{2,}\w*\b)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"111"+"00"*256+"! _1_EOA(iii)"
 */
var REGEX = /(?:\b\w*(\w\w?)\1{2,}\w*\b)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '111' + '00'.repeat(i*1) + '! _1_EOA(iii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}