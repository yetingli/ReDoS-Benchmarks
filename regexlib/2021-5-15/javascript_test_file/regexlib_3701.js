/* 3701
 * ^\s*[a-zA-Z\s]+\,[0-9\s]+\s*$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"a,"+"\t"*10000+"!_1_POA(i)"
 */
var REGEX = /^\s*[a-zA-Z\s]+\,[0-9\s]+\s*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'a,' + '\t'.repeat(i*10000) + '!_1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}