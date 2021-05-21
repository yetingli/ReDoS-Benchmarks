/* 3647
 * ^/{1}(((/{1}\.{1})?[a-zA-Z0-9 ]+/?)+(\.{1}[a-zA-Z0-9]{2,4})?)$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"/"+"a"*32+"◎@! _1_NQ"
 */
var REGEX = new RegExp("^/{1}(((/{1}\.{1})?[a-zA-Z0-9 ]+/?)+(\.{1}[a-zA-Z0-9]{2,4})?)$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '/' + 'a'.repeat(i*1) + '◎@! _1_NQ'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}