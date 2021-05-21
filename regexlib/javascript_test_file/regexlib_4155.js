/* 4155
 * ^[ \w]{3,}([A-Za-z]\.)?([ \w]*\#\d+)?(\r\n| )[ \w]{3,}[\/]
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"   "*5000+"!1 __POA(i)"
 */
var REGEX = new RegExp("^[ \w]{3,}([A-Za-z]\.)?([ \w]*\#\d+)?(\r\n| )[ \w]{3,}[\/]")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '   '.repeat(i*10000) + '!1 __POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}