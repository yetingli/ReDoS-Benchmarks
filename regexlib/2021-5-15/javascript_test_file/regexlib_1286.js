/* 1286
 * &lt;select(.|\n)*?selected(.|\n)*?&gt;(.*?)&lt;/option&gt;(.|\n)*?&lt;/select&gt;
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"&lt;selectselected&gt;"*128+"! _1SLQ_2"
 */
var REGEX = new RegExp("&lt;select(.|\n)*?selected(.|\n)*?&gt;(.*?)&lt;/option&gt;(.|\n)*?&lt;/select&gt;")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '&lt;selectselected&gt;'.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}