/* 294
 * ^\s*([\(]?)\[?\s*\d{3}\s*\]?[\)]?\s*[\-]?[\.]?\s*\d{3}\s*[\-]?[\.]?\s*\d{4}$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"111111"+"\t"*10000+"!_1_POA(i)"
 */
var REGEX = /^\s*([\(]?)\[?\s*\d{3}\s*\]?[\)]?\s*[\-]?[\.]?\s*\d{3}\s*[\-]?[\.]?\s*\d{4}$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '111111' + '\t'.repeat(i*10000) + '!_1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}