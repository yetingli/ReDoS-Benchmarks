/* 3613
 * <(?<tag>\w*|\w*\.+\w*)>+((.|[\n\t\f\r\s])*?)<\/\k<tag>>
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"<>"+"\t\t"*16+"! _1_EOD(i2)"
 */
var REGEX = new RegExp("<(?<tag>\w*|\w*\.+\w*)>+((.|[\n\t\f\r\s])*?)<\/\k<tag>>")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '<>' + '\t\t'.repeat(i*1) + '! _1_EOD(i2)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}