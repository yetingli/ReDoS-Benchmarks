/* 7838
 * \w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"1"*10000+"!1 _SLQ_1"
 */
var REGEX = /\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '1'.repeat(i*10000) + '!1 _SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}