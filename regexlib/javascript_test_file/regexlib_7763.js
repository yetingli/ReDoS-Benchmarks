/* 7763
 * <(?<tag>.*).*>(?<text>.*)</\k<tag>>
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"<></"*128+"! _1SLQ_2"
 */
var REGEX = new RegExp("<(?<tag>.*).*>(?<text>.*)</\k<tag>>")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '<></'.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}