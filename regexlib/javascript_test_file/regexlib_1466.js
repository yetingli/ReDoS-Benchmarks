/* 1466
 * ^((?:(?:(?:\w[\.\-\+]?)*)\w)+)\@((?:(?:(?:\w[\.\-\+]?){0,62})\w)+)\.(\w{2,6})$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"1@"+"0"*32+"! _1_EOA(iii)"
 */
var REGEX = /^((?:(?:(?:\w[\.\-\+]?)*)\w)+)\@((?:(?:(?:\w[\.\-\+]?){0,62})\w)+)\.(\w{2,6})$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '1@' + '0'.repeat(i*1) + '! _1_EOA(iii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}