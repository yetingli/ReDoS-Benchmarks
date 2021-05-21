/* 6153
 * ([^_.]([a-zA-Z0-9_]*[.]?[a-zA-Z0-9_]+[^_]){2})@([a-z0-9]+[.]([a-z]{2,3}|[a-z]{2,3}[.][a-z]{2,3}))
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"@a@a@"+"0000"*32+"◎1 __EOA(iii)"
 */
var REGEX = /([^_.]([a-zA-Z0-9_]*[.]?[a-zA-Z0-9_]+[^_]){2})@([a-z0-9]+[.]([a-z]{2,3}|[a-z]{2,3}[.][a-z]{2,3}))/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '@a@a@' + '0000'.repeat(i*1) + '◎1 __EOA(iii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}