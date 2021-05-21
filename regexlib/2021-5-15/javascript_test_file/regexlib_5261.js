/* 5261
 * ((\d{1,5})*\.*(\d{0,3})"[W|D|H|DIA][X|\s]).*
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"0"*32+"! _1_NQ"
 */
var REGEX = /((\d{1,5})*\.*(\d{0,3})"[W|D|H|DIA][X|\s]).*/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '0'.repeat(i*1) + '! _1_NQ'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}