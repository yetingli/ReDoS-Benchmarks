/* 5839
 * &lt;(?:[^&quot;']+?|.+?(?:&quot;|').*?(?:&quot;|')?.*?)*?&gt;
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"&lt;"+"'"*2+"! _1! _1! _1! _1! _1!\n_SLQ_3"
 */
var REGEX = /&lt;(?:[^&quot;']+?|.+?(?:&quot;|').*?(?:&quot;|')?.*?)*?&gt;/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '&lt;' + '\''.repeat(i*1) + '! _1! _1! _1! _1! _1!\n_SLQ_3'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}