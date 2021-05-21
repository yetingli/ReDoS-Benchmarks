/* 1802
 * (\[(\w+)\s*(([\w]*)=('|&quot;)?([a-zA-Z0-9|:|\/|=|-|.|\?|&amp;]*)(\5)?)*\])([a-zA-Z0-9|:|\/|=|-|.|\?|&amp;|\s]+)(\[\/\2\])
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"[1"+"=&quot;"*16+"◎@! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("(\[(\w+)\s*(([\w]*)=('|&quot;)?([a-zA-Z0-9|:|\/|=|-|.|\?|&amp;]*)(\5)?)*\])([a-zA-Z0-9|:|\/|=|-|.|\?|&amp;|\s]+)(\[\/\2\])")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '[1' + '=&quot;'.repeat(i*1) + '◎@! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}