/* 8048
 * ^(http(s?):\/\/)(www.)?(\w|-)+(\.(\w|-)+)*((\.[a-zA-Z]{2,3})|\.(aero|coop|info|museum|name))+(\/)?$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"http://1"+".aero.AA"*1024+"! _1_EOD(i2)"
 */
var REGEX = new RegExp("^(http(s?):\/\/)(www.)?(\w|-)+(\.(\w|-)+)*((\.[a-zA-Z]{2,3})|\.(aero|coop|info|museum|name))+(\/)?$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'http://1' + '.aero.AA'.repeat(i*1) + '! _1_EOD(i2)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}