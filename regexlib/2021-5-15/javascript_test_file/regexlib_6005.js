/* 6005
 * ^0$|^0\.{1}(\d{1,2})$|^[1-9]{1}[0-9]*\.?(\d{1,2})$|^[1-9]+[0-9]*$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"1"+"1"*10000+"! _1_POA(i)"
 */
var REGEX = /^0$|^0\.{1}(\d{1,2})$|^[1-9]{1}[0-9]*\.?(\d{1,2})$|^[1-9]+[0-9]*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '1' + '1'.repeat(i*10000) + '! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}