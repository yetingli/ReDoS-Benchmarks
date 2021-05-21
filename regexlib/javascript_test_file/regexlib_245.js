/* 245
 * ^(http(s?)\:\/\/)?(www.)?(([A-Za-z]+)([0-9]+)?([A-Za-z0-9\.\_\-]+)?)(\.)(([a-zA-Z]{2,})([0-9a-zA-Z]+)?)(\:\d{0,5})?(\/|(\/[A-Za-z]+([a-zA-Z0-9]+)?)+)?(\?[a-zA-Z0-9\\\&\%\_\.\/\-\=\~\*]+)?$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"A.aa"+"/AA"*32+"! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("^(http(s?)\:\/\/)?(www.)?(([A-Za-z]+)([0-9]+)?([A-Za-z0-9\.\_\-]+)?)(\.)(([a-zA-Z]{2,})([0-9a-zA-Z]+)?)(\:\d{0,5})?(\/|(\/[A-Za-z]+([a-zA-Z0-9]+)?)+)?(\?[a-zA-Z0-9\\\&\%\_\.\/\-\=\~\*]+)?$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'A.aa' + '/AA'.repeat(i*1) + '! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}