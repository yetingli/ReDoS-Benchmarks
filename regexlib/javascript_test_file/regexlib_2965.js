/* 2965
 * &lt;(\/{0,1})img(.*?)(\/{0,1})\&gt;
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"&lt;img"*5000+"! _1SLQ_2"
 */
var REGEX = new RegExp("&lt;(\/{0,1})img(.*?)(\/{0,1})\&gt;")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '&lt;img'.repeat(i*10000) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}