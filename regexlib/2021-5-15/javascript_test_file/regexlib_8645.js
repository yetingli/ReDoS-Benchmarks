/* 8645
 * [\(]{1,}[^)]*[)]{1,}
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"("*1024+"@1 _SLQ_1"
 */
var REGEX = /[\(]{1,}[^)]*[)]{1,}/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '('.repeat(i*1) + '@1 _SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}