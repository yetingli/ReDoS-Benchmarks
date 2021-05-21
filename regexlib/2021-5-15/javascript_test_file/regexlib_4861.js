/* 4861
 * ^[0-9]{6}-(?:[0-9]+){1,3}[0-9A-Za-z]$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"000000-"+"0"*512+"!1 __NQ"
 */
var REGEX = /^[0-9]{6}-(?:[0-9]+){1,3}[0-9A-Za-z]$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '000000-' + '0'.repeat(i*1) + '!1 __NQ'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}