/* 7094
 * ^([a-zA-Z0-9]+[._-])*[a-zA-Z0-9]+@(([a-zA-Z0-9]+|([a-zA-Z0-9]+[.-])+)[a-zA-Z0-9]+\.[a-zA-Z]{2,4}|([a-zA-Z]\.com))$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"a@"+"a"*10000+"!1 _SLQ_2"
 */
var REGEX = /^([a-zA-Z0-9]+[._-])*[a-zA-Z0-9]+@(([a-zA-Z0-9]+|([a-zA-Z0-9]+[.-])+)[a-zA-Z0-9]+\.[a-zA-Z]{2,4}|([a-zA-Z]\.com))$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'a@' + 'a'.repeat(i*10000) + '!1 _SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}