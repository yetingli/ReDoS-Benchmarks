/* 4820
 * ([0-9a-zA-Z]+)|([0-9a-zA-Z][0-9a-zA-Z\\s]+[0-9a-zA-Z]+)
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"0"*10000+"SLQ_1"
 */
var REGEX = /([0-9a-zA-Z]+)|([0-9a-zA-Z][0-9a-zA-Z\\s]+[0-9a-zA-Z]+)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '0'.repeat(i*10000) + 'SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}