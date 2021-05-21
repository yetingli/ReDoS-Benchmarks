/* 6998
 * .*[\$Ss]pecia[l1]\W[Oo0]ffer.*
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"$pecial$Offer"*5000+"! _1SLQ_2\n"
 */
var REGEX = /.*[\$Ss]pecia[l1]\W[Oo0]ffer.*/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '$pecial$Offer'.repeat(i*10000) + '! _1SLQ_2\n'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}