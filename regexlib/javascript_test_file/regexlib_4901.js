/* 4901
 * ^\s*-?((\d{1,3}(\.(\d){3})*)|\d*)(,\d{1,2})?\s?(\u20AC)?\s*$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"\t"*10000+"!_1_POA(i)"
 */
var REGEX = /^\s*-?((\d{1,3}(\.(\d){3})*)|\d*)(,\d{1,2})?\s?(\u20AC)?\s*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '\t'.repeat(i*10000) + '!_1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}