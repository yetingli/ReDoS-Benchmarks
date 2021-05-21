/* 6858
 * \b[\w]+[\w.-][\w]+@[\w]+[\w.-]\.[\w]{2,4}\b
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"11"*5000+"!1 _SLQ_2"
 */
var REGEX = /\b[\w]+[\w.-][\w]+@[\w]+[\w.-]\.[\w]{2,4}\b/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '11'.repeat(i*10000) + '!1 _SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}