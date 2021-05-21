/* 5965
 * <\s*/?\s*\w+(\s*\w+\s*=\s*(['"][^'"]*['"]|[\w#]+))*\s*/?\s*>
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"<1"+"000="*32+"! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("<\s*/?\s*\w+(\s*\w+\s*=\s*(['"][^'"]*['"]|[\w#]+))*\s*/?\s*>")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '<1' + '000='.repeat(i*1) + '! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}