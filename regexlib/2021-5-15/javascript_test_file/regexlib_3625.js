/* 3625
 * ^[a-zA-Z_:]+[a-zA-Z_:\-\.\d]*$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"a"*10000+"!1 _SLQ_2"
 */
var REGEX = /^[a-zA-Z_:]+[a-zA-Z_:\-\.\d]*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'a'.repeat(i*10000) + '!1 _SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}