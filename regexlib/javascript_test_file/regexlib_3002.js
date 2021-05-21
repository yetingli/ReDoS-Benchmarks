/* 3002
 * [A-Za-z_.0-9-]+@{1}[a-z]+([.]{1}[a-z]{2,4})+
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"A"*10000+"! _1SLQ_1"
 */
var REGEX = /[A-Za-z_.0-9-]+@{1}[a-z]+([.]{1}[a-z]{2,4})+/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'A'.repeat(i*10000) + '! _1SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}