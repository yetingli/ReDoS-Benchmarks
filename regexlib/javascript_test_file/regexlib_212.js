/* 212
 * ^[\n &lt;&quot;']*([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+)
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"l"*10000+"!1 __POA(i)"
 */
var REGEX = /^[\n &lt;&quot;']*([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'l'.repeat(i*10000) + '!1 __POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}