/* 1287
 * &lt;textarea(.|\n)*?&gt;((.|\n)*?)&lt;/textarea&gt;
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"&lt;textarea"+"&gt;"*5000+"! _1_POA(i)"
 */
var REGEX = new RegExp("&lt;textarea(.|\n)*?&gt;((.|\n)*?)&lt;/textarea&gt;")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '&lt;textarea' + '&gt;'.repeat(i*10000) + '! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}