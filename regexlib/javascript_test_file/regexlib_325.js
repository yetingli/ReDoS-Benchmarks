/* 325
 * ^\w+\W+[a-z]\W+(\w+)([a-z])(\w+)\s\&\s\w+\W+[a-z]\W+\1(?!\2)[a-z]\3$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"1:a:"+"v"*10000+"! _1_POA(i)"
 */
var REGEX = /^\w+\W+[a-z]\W+(\w+)([a-z])(\w+)\s\&\s\w+\W+[a-z]\W+\1(?!\2)[a-z]\3$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '1:a:' + 'v'.repeat(i*10000) + '! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}