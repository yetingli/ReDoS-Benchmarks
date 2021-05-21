/* 3759
 * (?<prefix>[\d]{3})[\s+\/\\\-]+(?<number>[\d\-\s]+)
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"111"+"\t"*10000+"!1 __POA(i)"
 */
var REGEX = new RegExp("(?<prefix>[\d]{3})[\s+\/\\\-]+(?<number>[\d\-\s]+)")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '111' + '\t'.repeat(i*10000) + '!1 __POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}