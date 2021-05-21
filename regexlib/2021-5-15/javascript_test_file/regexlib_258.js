/* 258
 * (?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}\.?\t*\s*){2}\(\r*\n*([0-9]{1,})
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"a.aa"*128+"!_1SLQ_2"
 */
var REGEX = /(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}\.?\t*\s*){2}\(\r*\n*([0-9]{1,})/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'a.aa'.repeat(i*1) + '!_1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}