/* 6148
 * <(\w+)(\s(\w*=".*?")?)*((/>)|((/*?)>.*?</\1>))
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"<1"+"\t0="""*32+"! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("<(\w+)(\s(\w*=".*?")?)*((/>)|((/*?)>.*?</\1>))")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '<1' + '\t0=\"\"'.repeat(i*1) + '! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}