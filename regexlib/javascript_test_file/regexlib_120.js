/* 120
 * &lt;/?(\w+)(\s*\w*\s*=\s*(&quot;[^&quot;]*&quot;|'[^']'|[^&gt;]*))*|/?&gt;
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"&lt;1"+"\t=&quot;&quot;"*32+"! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("&lt;/?(\w+)(\s*\w*\s*=\s*(&quot;[^&quot;]*&quot;|'[^']'|[^&gt;]*))*|/?&gt;")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '&lt;1' + '\t=&quot;&quot;'.repeat(i*1) + '! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}