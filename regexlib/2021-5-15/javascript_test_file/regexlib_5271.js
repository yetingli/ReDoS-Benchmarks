/* 5271
 * (\s*\S*){2}(ipsum)(\S*\s*){2}
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"\t"*512+"!_1_NQ"
 */
var REGEX = /(\s*\S*){2}(ipsum)(\S*\s*){2}/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '\t'.repeat(i*1) + '!_1_NQ'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}