/* 4785
 * (<input )(.*?)(>)
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"<input "*5000+"! _1SLQ_2"
 */
var REGEX = /(<input )(.*?)(>)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '<input '.repeat(i*10000) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}