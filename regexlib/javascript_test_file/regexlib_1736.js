/* 1736
 * (((s*)(ftp)(s*)|(http)(s*)|mailto|news|file|webcal):(\S*))|((www.)(\S*))
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"s"*10000+"! _1! _1SLQ_1"
 */
var REGEX = /(((s*)(ftp)(s*)|(http)(s*)|mailto|news|file|webcal):(\S*))|((www.)(\S*))/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 's'.repeat(i*10000) + '! _1! _1SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}