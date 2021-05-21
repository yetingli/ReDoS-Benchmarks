/* 7600
 * ^[a-z]+([a-z0-9-]*[a-z0-9]+)?(\.([a-z]+([a-z0-9-]*[a-z0-9]+)?)+)*$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"a."+"aa"*8+"!1 __EOA(i or ii)"
 */
var REGEX = /^[a-z]+([a-z0-9-]*[a-z0-9]+)?(\.([a-z]+([a-z0-9-]*[a-z0-9]+)?)+)*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'a.' + 'aa'.repeat(i*1) + '!1 __EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}