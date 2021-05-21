/* 8359
 * ^\d+?[A-Za-z]*\s\w*\s?\w+?\s\w{2}\w*\s*\w*$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"1 1 11"+"00"*5000+"! _1_POA(i)"
 */
var REGEX = /^\d+?[A-Za-z]*\s\w*\s?\w+?\s\w{2}\w*\s*\w*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '1 1 11' + '00'.repeat(i*10000) + '! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}