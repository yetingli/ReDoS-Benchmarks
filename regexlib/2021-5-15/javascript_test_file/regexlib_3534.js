/* 3534
 * ^[\u0600-\u06ff\s]+$|[\u0750-\u077f\s]+$|[\ufb50-\ufc3f\s]+$|[\ufe70-\ufefc\s]+$|[\u06cc\s]+$|[\u067e\s]+$|[\u06af\s]$|[\u0691\s]+$|^$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"ݿ"*20000+"!1 _SLQ_1"
 */
var REGEX = /^[\u0600-\u06ff\s]+$|[\u0750-\u077f\s]+$|[\ufb50-\ufc3f\s]+$|[\ufe70-\ufefc\s]+$|[\u06cc\s]+$|[\u067e\s]+$|[\u06af\s]$|[\u0691\s]+$|^$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'ݿ'.repeat(i*10000) + '!1 _SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}