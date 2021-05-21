/* 5473
 * ^\s*([A-Z\s])([a-z\s]){1,30}([A-Z\s])([a-z\s]){1,30}\s*$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"A"+"\t\t"*20000+"!_1_POA(i)"
 */
var REGEX = /^\s*([A-Z\s])([a-z\s]){1,30}([A-Z\s])([a-z\s]){1,30}\s*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'A' + '\t\t'.repeat(i*10000) + '!_1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}