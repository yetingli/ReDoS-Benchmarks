/* 8197
 * ^([A-Z]{1,}[a-z]{1,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,})$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"A"+"a"*5000+"!1 __POA(i)"
 */
var REGEX = /^([A-Z]{1,}[a-z]{1,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,}[A-Z]{0,}[a-z]{0,})$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'A' + 'a'.repeat(i*10000) + '!1 __POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}