/* 3748
 * ^(?:[\w]+[\&amp;\-_\.]*)+@(?:(?:[\w]+[\-_\.]*)\.(?:[a-zA-Z]{2,}?))$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"__"*16+"!1 __EOA(i or ii)"
 */
var REGEX = /^(?:[\w]+[\&amp;\-_\.]*)+@(?:(?:[\w]+[\-_\.]*)\.(?:[a-zA-Z]{2,}?))$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '__'.repeat(i*1) + '!1 __EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}