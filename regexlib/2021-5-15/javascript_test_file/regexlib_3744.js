/* 3744
 * ^Content-Type:\s*(\w+)\s*/?\s*(\w*)?\s*;\s*((\w+)?\s*=\s*((".+")|(\S+)))?
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"Content-Type:1"+"\t"*5000+"! _1_POA(i)"
 */
var REGEX = new RegExp("^Content-Type:\s*(\w+)\s*/?\s*(\w*)?\s*;\s*((\w+)?\s*=\s*((".+")|(\S+)))?")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'Content-Type:1' + '\t'.repeat(i*10000) + '! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}