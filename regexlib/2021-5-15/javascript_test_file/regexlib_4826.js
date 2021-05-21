/* 4826
 * (?=^.{1,254}$)(^(?:[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]\.?)+(?:[a-zA-Z]{2,})$)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"0"*32+"! _1_EOA(iv)"
 */
var REGEX = /(?=^.{1,254}$)(^(?:[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]\.?)+(?:[a-zA-Z]{2,})$)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '0'.repeat(i*1) + '! _1_EOA(iv)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}