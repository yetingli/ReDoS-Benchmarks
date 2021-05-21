/* 8480
 * (http://|)(www\.)?([^\.]+)\.(\w{2}|(com|net|org|edu|int|mil|gov|arpa|biz|aero|name|coop|info|pro|museum))$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"http://"*5000+"! _1_POA(i)"
 */
var REGEX = new RegExp("(http://|)(www\.)?([^\.]+)\.(\w{2}|(com|net|org|edu|int|mil|gov|arpa|biz|aero|name|coop|info|pro|museum))$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'http://'.repeat(i*10000) + '! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}