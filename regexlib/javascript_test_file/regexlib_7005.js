/* 7005
 * ^(\d|,)*\d*$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"8"*10000+"! _1! _1!\n_SLQ_3"
 */
var REGEX = /^(\d|,)*\d*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '8'.repeat(i*10000) + '! _1! _1!\n_SLQ_3'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}