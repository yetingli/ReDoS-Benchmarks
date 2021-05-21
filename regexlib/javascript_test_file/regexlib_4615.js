/* 4615
 * &amp;lt;/?([a-zA-Z][-A-Za-z\d\.]{0,71})(\s+(\S+)(\s*=\s*([-\w\.]{1,1024}|&amp;quot;[^&amp;quot;]{0,1024}&amp;quot;|'[^']{0,1024}'))?)*\s*&amp;gt;
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"&amp;lt;a &"+"\t=''"*32+"! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("&amp;lt;/?([a-zA-Z][-A-Za-z\d\.]{0,71})(\s+(\S+)(\s*=\s*([-\w\.]{1,1024}|&amp;quot;[^&amp;quot;]{0,1024}&amp;quot;|'[^']{0,1024}'))?)*\s*&amp;gt;")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '&amp;lt;a &' + '\t=\'\''.repeat(i*1) + '! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}