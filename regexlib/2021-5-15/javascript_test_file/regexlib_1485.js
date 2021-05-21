/* 1485
 * &lt;a [a-zA-Z0-9 =&quot;'.:;?]*href=*[a-zA-Z0-9 =&quot;'.:;&gt;?]*[^&gt;]*&gt;([a-zA-Z0-9 =&quot;'.:;&gt;?]*[^&lt;]*&lt;)\s*/a\s*&gt;
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"&lt;a href"*256+"@1 _SLQ_2"
 */
var REGEX = new RegExp("&lt;a [a-zA-Z0-9 =&quot;'.:;?]*href=*[a-zA-Z0-9 =&quot;'.:;&gt;?]*[^&gt;]*&gt;([a-zA-Z0-9 =&quot;'.:;&gt;?]*[^&lt;]*&lt;)\s*/a\s*&gt;")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '&lt;a href'.repeat(i*1) + '@1 _SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}