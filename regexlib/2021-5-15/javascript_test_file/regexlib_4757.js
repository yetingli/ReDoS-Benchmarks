/* 4757
 * ^([0-9a-zA-Z]+|[a-zA-Z]:(\\(\w[\w ]*.*))+|\\(\\(\w[\w ]*.*))+)\.[0-9a-zA-Z]{1,3}$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"\\\\0a:\\1"+"1"*5000+"! _1SLQ_2"
 */
var REGEX = /^([0-9a-zA-Z]+|[a-zA-Z]:(\\(\w[\w ]*.*))+|\\(\\(\w[\w ]*.*))+)\.[0-9a-zA-Z]{1,3}$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '\\\\0a:\\1' + '1'.repeat(i*10000) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}