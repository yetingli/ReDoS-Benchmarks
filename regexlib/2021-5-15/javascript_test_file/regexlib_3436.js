/* 3436
 * \(?\s*(?<area>\d{3})\s*[\)\.\-]?\s*(?<first>\d{3})\s*[\-\.]?\s*(?<second>\d{4})\D*(?<ext>\d*)
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"111"+"\t"*5000+"◎@! _1_POA(i)"
 */
var REGEX = /\(?\s*(?<area>\d{3})\s*[\)\.\-]?\s*(?<first>\d{3})\s*[\-\.]?\s*(?<second>\d{4})\D*(?<ext>\d*)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '111' + '\t'.repeat(i*10000) + '◎@! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}