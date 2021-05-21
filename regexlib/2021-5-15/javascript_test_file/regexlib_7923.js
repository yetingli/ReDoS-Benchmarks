/* 7923
 * &lt;asp:requiredfieldvalidator(\s*\w+\s*=\s*\&quot;?\s*\w+\s*\&quot;?\s*)+\s*&gt;\s*&lt;\/asp:requiredfieldvalidator&gt;
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"&lt;asp:requiredfieldvalidator"+"\t0=&quot0&quot"*32+"! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("&lt;asp:requiredfieldvalidator(\s*\w+\s*=\s*\&quot;?\s*\w+\s*\&quot;?\s*)+\s*&gt;\s*&lt;\/asp:requiredfieldvalidator&gt;")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '&lt;asp:requiredfieldvalidator' + '\t0=&quot0&quot'.repeat(i*1) + '! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}