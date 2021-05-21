/* 7107
 * &lt;[aA][ ]{0,}([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,}&gt;((&lt;(([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,})&gt;([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,})|(([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,})){0,}
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"&lt;a"+" "*5000+"! _1_POA(i)"
 */
var REGEX = new RegExp("&lt;[aA][ ]{0,}([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,}&gt;((&lt;(([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,})&gt;([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,})|(([a-zA-Z0-9&quot;'_,.:;!?@$&amp;()%=/ ]|[-]|[	\f]){0,})){0,}")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '&lt;a' + ' '.repeat(i*10000) + '! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}