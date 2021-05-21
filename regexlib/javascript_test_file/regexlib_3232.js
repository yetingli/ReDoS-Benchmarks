/* 3232
 * [a-z0-9][a-z0-9_\.-]{0,}[a-z0-9]\.[a-z0-9][a-z0-9_\.-]{0,}[a-z0-9][\.][cn]{2,4}
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"a"+"0.0"*5000+"!1 __POA(i)"
 */
var REGEX = /[a-z0-9][a-z0-9_\.-]{0,}[a-z0-9]\.[a-z0-9][a-z0-9_\.-]{0,}[a-z0-9][\.][cn]{2,4}/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'a' + '0.0'.repeat(i*10000) + '!1 __POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}