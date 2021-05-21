/* 1167
 * ^(([a-zA-Z0-9]+([\-])?[a-zA-Z0-9]+)+(\.)?)+[a-zA-Z]{2,6}$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"000"*8+"!1 __EOA(i or ii)"
 */
var REGEX = /^(([a-zA-Z0-9]+([\-])?[a-zA-Z0-9]+)+(\.)?)+[a-zA-Z]{2,6}$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '000'.repeat(i*1) + '!1 __EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}