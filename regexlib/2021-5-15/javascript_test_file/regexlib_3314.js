/* 3314
 * ^([\u00c0-\u01ffa-zA-Z'\-]+[ ]?[\u00c0-\u01ffa-zA-Z'\-]*)+$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"''"*8+"!1 __EOA(i or ii)"
 */
var REGEX = /^([\u00c0-\u01ffa-zA-Z'\-]+[ ]?[\u00c0-\u01ffa-zA-Z'\-]*)+$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '\'\''.repeat(i*1) + '!1 __EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}