/* 2351
 * &lt;a[\s]+[^&gt;]*?href[\s]?=[\s\&quot;\']+(.*?)[\&quot;\']+.*?&gt;([^&lt;]+|.*?)?&lt;\/a&gt;
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"&lt;a href= &"*128+"! _1SLQ_2"
 */
var REGEX = new RegExp("&lt;a[\s]+[^&gt;]*?href[\s]?=[\s\&quot;\']+(.*?)[\&quot;\']+.*?&gt;([^&lt;]+|.*?)?&lt;\/a&gt;")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '&lt;a href= &'.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}