/* 7018
 * ^([a-zA-Z](?:(?:(?:\w[\.\_]?)*)\w)+)([a-zA-Z0-9])$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"a"+"_"*32+"!1 __EOA(iii)"
 */
var REGEX = /^([a-zA-Z](?:(?:(?:\w[\.\_]?)*)\w)+)([a-zA-Z0-9])$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'a' + '_'.repeat(i*1) + '!1 __EOA(iii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}