/* 5275
 * ^([1-9]{1}(([0-9])?){2})+(,[0-9]{1}[0-9]{2})*$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"1"*32+"!1 __EOA(iii)"
 */
var REGEX = /^([1-9]{1}(([0-9])?){2})+(,[0-9]{1}[0-9]{2})*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '1'.repeat(i*1) + '!1 __EOA(iii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}