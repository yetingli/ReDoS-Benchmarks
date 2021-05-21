/* 1123
 * (\s(\bon[a-zA-Z][a-z]+)\s?\=\s?[\'\"]?(javascript\:)?[\w\(\),\' ]*;?[\'\"]?)+
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"\tonAa='"*16+"!_1_EOA(i or ii)"
 */
var REGEX = /(\s(\bon[a-zA-Z][a-z]+)\s?\=\s?[\'\"]?(javascript\:)?[\w\(\),\' ]*;?[\'\"]?)+/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '\tonAa=\''.repeat(i*1) + '!_1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}