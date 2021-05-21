/* 1641
 * <a\s+(?:(?:\w+\s*=\s*)(?:\w+|"[^"]*"|'[^']*'))*?\s*href\s*=\s*(?<url>\w+|"[^"]*"|'[^']*')(?:(?:\s+\w+\s*=\s*)(?:\w+|"[^"]*"|'[^']*'))*?>.+?</a>
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"<a "+"000="*32+"! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("<a\s+(?:(?:\w+\s*=\s*)(?:\w+|"[^"]*"|'[^']*'))*?\s*href\s*=\s*(?<url>\w+|"[^"]*"|'[^']*')(?:(?:\s+\w+\s*=\s*)(?:\w+|"[^"]*"|'[^']*'))*?>.+?</a>")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '<a ' + '000='.repeat(i*1) + '! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}