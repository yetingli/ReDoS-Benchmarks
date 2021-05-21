/* 3617
 * ^START(?=(?:.(?!END|START))*MIDDLE).*?END[^\n]+
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"START=MIDDLEEND"*5000+"@1 _SLQ_2\n"
 */
var REGEX = /^START(?=(?:.(?!END|START))*MIDDLE).*?END[^\n]+/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'START=MIDDLEEND'.repeat(i*10000) + '@1 _SLQ_2\n'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}