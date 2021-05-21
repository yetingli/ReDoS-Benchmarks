/* 3180
 * ^(([a-zA-Z]:)|(\\{2}\w+)\$?)(\\(\w[\w ]*.*))+\.(jpg|JPG)$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"a:"+"\\0 0"*16+"!1 __EOA(i or ii)"
 */
var REGEX = /^(([a-zA-Z]:)|(\\{2}\w+)\$?)(\\(\w[\w ]*.*))+\.(jpg|JPG)$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'a:' + '\\0 0'.repeat(i*1) + '!1 __EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}