/* 6844
 * [ ]*=[ ]*[\&quot;]*cid[ ]*:[ ]*([^\&quot;&lt;&gt; ]+)
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+" "*20000+"! _1SLQ_1q"
 */
var REGEX = /[ ]*=[ ]*[\&quot;]*cid[ ]*:[ ]*([^\&quot;&lt;&gt; ]+)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + ' '.repeat(i*10000) + '! _1SLQ_1q'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}