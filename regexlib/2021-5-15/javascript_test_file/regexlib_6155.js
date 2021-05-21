/* 6155
 * (?:\d|I{1,3})?\s?\w{2,}\.?\s*\d{1,}\:\d{1,}-?,?\d{0,2}(?:,\d{0,2}){0,2}
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"11"*512+"!_1SLQ_2"
 */
var REGEX = /(?:\d|I{1,3})?\s?\w{2,}\.?\s*\d{1,}\:\d{1,}-?,?\d{0,2}(?:,\d{0,2}){0,2}/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '11'.repeat(i*1) + '!_1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}