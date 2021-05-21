/* 2762
 * ([0-9]+:)?[0-9]+\s*(am|pm)|[0-9]+:[0-9]+\s*(am|pm)?
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"0"*5000+"!_1SLQ_2"
 */
var REGEX = /([0-9]+:)?[0-9]+\s*(am|pm)|[0-9]+:[0-9]+\s*(am|pm)?/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '0'.repeat(i*10000) + '!_1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}