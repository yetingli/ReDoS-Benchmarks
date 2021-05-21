/* 228
 * ^([A-Za-z]|[A-Za-z][0-9]*|[0-9]*[A-Za-z])+$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"AA"*8+"!1 __EOD(ii2)"
 */
var REGEX = /^([A-Za-z]|[A-Za-z][0-9]*|[0-9]*[A-Za-z])+$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'AA'.repeat(i*1) + '!1 __EOD(ii2)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}