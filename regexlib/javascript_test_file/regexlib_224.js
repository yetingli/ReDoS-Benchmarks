/* 224
 * (?:(?:http|https)://(?:(?:[^/&=()/§, ]*?)*\.)+(?:\w{2,3})+?)(?:/+[^ ?,'§$&()={\[\]}]*)*(?:\?+.*)?$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"http://."*80000+"! _1SLQ_2"
 */
var REGEX = new RegExp("(?:(?:http|https)://(?:(?:[^/&=()/§, ]*?)*\.)+(?:\w{2,3})+?)(?:/+[^ ?,'§$&()={\[\]}]*)*(?:\?+.*)?$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'http://.'.repeat(i*10000) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}