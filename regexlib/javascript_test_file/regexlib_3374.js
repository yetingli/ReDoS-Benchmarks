/* 3374
 * ^([A-Z]{3,20}\s?[A-Z]{2}[0-9]{1,3}-([A-Z]{3}|[A-Z]{1}[0-9]{2}))|([A-Z]{1,20}\s[A-Z]{1,2}[0-9]{1,4}-[A-Z]{1,3})|([\d,\w,\s]{1,20}\s[A-Z]{3}-[0-9]{1,3})|([A-Z]{1,20}\s?[\d,\w,\s]{1,20})$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"A"*80000+"!_1SLQ_1"
 */
var REGEX = /^([A-Z]{3,20}\s?[A-Z]{2}[0-9]{1,3}-([A-Z]{3}|[A-Z]{1}[0-9]{2}))|([A-Z]{1,20}\s[A-Z]{1,2}[0-9]{1,4}-[A-Z]{1,3})|([\d,\w,\s]{1,20}\s[A-Z]{3}-[0-9]{1,3})|([A-Z]{1,20}\s?[\d,\w,\s]{1,20})$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'A'.repeat(i*10000) + '!_1SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}