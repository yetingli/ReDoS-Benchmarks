/* 5494
 * ^.*(?=.{6,10})(?=.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z])(?=.*\d.*\d).*$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"==111111=aaaa"+"1"*10000+"! _1SLQ_2"
 */
var REGEX = /^.*(?=.{6,10})(?=.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z])(?=.*\d.*\d).*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '==111111=aaaa' + '1'.repeat(i*10000) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}