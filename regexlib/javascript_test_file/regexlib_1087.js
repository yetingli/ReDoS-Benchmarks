/* 1087
 * ^[^']*?\&lt;\s*Assembly\s*:\s*AssemblyVersion\s*\(\s*&quot;(\*|[0-9]+.\*|[0-9]+.[0-9]+.\*|[0-9]+.[0-9]+.[0-9]+.\*|[0-9]+.[0-9]+.[0-9]+.[0-9]+)&quot;\s*\)\s*\&gt;.*$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"*01*0101*010101*&lt;Assembly:AssemblyVersion(&quot;"+"0101"*64+"!1 _SLQ_2"
 */
var REGEX = /^[^']*?\&lt;\s*Assembly\s*:\s*AssemblyVersion\s*\(\s*&quot;(\*|[0-9]+.\*|[0-9]+.[0-9]+.\*|[0-9]+.[0-9]+.[0-9]+.\*|[0-9]+.[0-9]+.[0-9]+.[0-9]+)&quot;\s*\)\s*\&gt;.*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '*01*0101*010101*&lt;Assembly:AssemblyVersion(&quot;' + '0101'.repeat(i*1) + '!1 _SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}