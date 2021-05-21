/* 8287
 * ^[a-z0-9_.-]*@[a-z0-9-]+(.[a-z]{2,4})+$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"@"+"aaa"*5000+"!1 __POA(i)"
 */
var REGEX = /^[a-z0-9_.-]*@[a-z0-9-]+(.[a-z]{2,4})+$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '@' + 'aaa'.repeat(i*10000) + '!1 __POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}