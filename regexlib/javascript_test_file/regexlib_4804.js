/* 4804
 * ^(\+[0-9]{2,}[0-9]{4,}[0-9]*)(x?[0-9]{1,})?$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"+00"+"0000"*5000+"◎@! _1_POA(i)"
 */
var REGEX = /^(\+[0-9]{2,}[0-9]{4,}[0-9]*)(x?[0-9]{1,})?$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '+00' + '0000'.repeat(i*10000) + '◎@! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}