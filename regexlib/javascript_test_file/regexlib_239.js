/* 239
 * ^[a-z]+([\d_-]*[a-z]+)*@[a-z]{2,}(\.)[a-z]{2,}(\.[a-z]{2})?$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"a"+"a"*32+"!1 __NQ"
 */
var REGEX = /^[a-z]+([\d_-]*[a-z]+)*@[a-z]{2,}(\.)[a-z]{2,}(\.[a-z]{2})?$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'a' + 'a'.repeat(i*1) + '!1 __NQ'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}