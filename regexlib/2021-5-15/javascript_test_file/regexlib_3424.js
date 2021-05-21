/* 3424
 * (\s*<(\w*)\s+(((\w*)(=["']?)([\w\W\d]*?)["']?)+)\s*/?>)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"< "+"0="*16+"!_1_EOA(i or ii)"
 */
var REGEX = new RegExp("(\s*<(\w*)\s+(((\w*)(=["']?)([\w\W\d]*?)["']?)+)\s*/?>)")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '< ' + '0='.repeat(i*1) + '!_1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}