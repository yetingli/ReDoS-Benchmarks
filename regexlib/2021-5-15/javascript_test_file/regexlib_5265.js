/* 5265
 * ^<\s*(td|TD)\s*(\w|\W)*\s*>(\w|\W)*</(td|TD)>$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"<td>"+"\t"*10000+"! _1_POA(i)"
 */
var REGEX = new RegExp("^<\s*(td|TD)\s*(\w|\W)*\s*>(\w|\W)*</(td|TD)>$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '<td>' + '\t'.repeat(i*10000) + '! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}