/* 5784
 * [a-zA-Z]{3,}://[a-zA-Z0-9\.]+/*[a-zA-Z0-9/\\%_.]*\?*[a-zA-Z0-9/\\%_.=&amp;]*
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"aaa"*5000+"! _1SLQ_1"
 */
var REGEX = new RegExp("[a-zA-Z]{3,}://[a-zA-Z0-9\.]+/*[a-zA-Z0-9/\\%_.]*\?*[a-zA-Z0-9/\\%_.=&amp;]*")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'aaa'.repeat(i*10000) + '! _1SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}