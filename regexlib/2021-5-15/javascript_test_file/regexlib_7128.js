/* 7128
 * ^(9|2{1})+([1-9]{1})+([0-9]{7})$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"9"*5000+"!1 _!1 _! _1!\n_SLQ_3"
 */
var REGEX = /^(9|2{1})+([1-9]{1})+([0-9]{7})$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '9'.repeat(i*10000) + '!1 _!1 _! _1!\n_SLQ_3'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}