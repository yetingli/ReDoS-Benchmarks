/* 2897
 * ('.*$|Rem((\t| ).*$|$)|&quot;(.|&quot;&quot;)*?&quot;)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"&quot;"+"&quot;"*32+"! _1_EOA(iv)"
 */
var REGEX = /('.*$|Rem((\t| ).*$|$)|&quot;(.|&quot;&quot;)*?&quot;)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '&quot;' + '&quot;'.repeat(i*1) + '! _1_EOA(iv)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}