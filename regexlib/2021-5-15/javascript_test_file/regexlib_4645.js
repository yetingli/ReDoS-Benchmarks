/* 4645
 * ^([1-9]+\d{0,2},(\d{3},)*\d{3}(\.\d{1,2})?|[1-9]+\d*(\.\d{1,2})?)$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"1"*5000+"!1 __POA(i)"
 */
var REGEX = /^([1-9]+\d{0,2},(\d{3},)*\d{3}(\.\d{1,2})?|[1-9]+\d*(\.\d{1,2})?)$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '1'.repeat(i*10000) + '!1 __POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}