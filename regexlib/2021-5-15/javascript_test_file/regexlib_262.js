/* 262
 * ([a-zA-Z]{1}[a-zA-Z]*[\s]{0,1}[a-zA-Z])+([\s]{0,1}[a-zA-Z]+)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"A"*64+"!1 __EOA(iv)"
 */
var REGEX = /([a-zA-Z]{1}[a-zA-Z]*[\s]{0,1}[a-zA-Z])+([\s]{0,1}[a-zA-Z]+)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'A'.repeat(i*1) + '!1 __EOA(iv)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}