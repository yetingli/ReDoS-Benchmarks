/* 7906
 * &lt;script[\s\S]*?&lt;/script([\s\S]*?)&gt;
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"&lt;script&lt;/script"*256+"! _1SLQ_2"
 */
var REGEX = new RegExp("&lt;script[\s\S]*?&lt;/script([\s\S]*?)&gt;")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '&lt;script&lt;/script'.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}