/* 1340
 * ((?<Owner>\[?[\w\d]+\]?)\.{1})?(?<Column>\[?[\w\d]+\]?)(\s*(([><=]{1,2})|(Not|In\(|Between){1,2})\s*)(?<Value>[\w\d\']+)
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"1Not"+"NotNot"*5000+"!1 _◎@! _1!\n_SLQ_3"
 */
var REGEX = /((?<Owner>\[?[\w\d]+\]?)\.{1})?(?<Column>\[?[\w\d]+\]?)(\s*(([><=]{1,2})|(Not|In\(|Between){1,2})\s*)(?<Value>[\w\d\']+)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '1Not' + 'NotNot'.repeat(i*10000) + '!1 _◎@! _1!\n_SLQ_3'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}