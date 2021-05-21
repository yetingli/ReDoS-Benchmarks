/* 3297
 * &lt;a[a-zA-Z0-9 =&quot;'.?_/]*(href\s*=\s*){1}[a-zA-Z0-9 =&quot;'.?_/]*\s*((/&gt;)|(&gt;[a-zA-Z0-9 =&quot;'&lt;&gt;.?_/]*&lt;/a&gt;))
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"/&gt;&lt;ahref="+"&gt;"*5000+"!1 _SLQ_2"
 */
var REGEX = new RegExp("&lt;a[a-zA-Z0-9 =&quot;'.?_/]*(href\s*=\s*){1}[a-zA-Z0-9 =&quot;'.?_/]*\s*((/&gt;)|(&gt;[a-zA-Z0-9 =&quot;'&lt;&gt;.?_/]*&lt;/a&gt;))")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '/&gt;&lt;ahref=' + '&gt;'.repeat(i*10000) + '!1 _SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}