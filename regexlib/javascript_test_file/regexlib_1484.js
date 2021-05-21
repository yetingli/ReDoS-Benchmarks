/* 1484
 * <a[a-zA-Z0-9 ="'.:;?]*(href=[\"\'](http:\/\/|\.\/|\/)?\w+(\.\w+)*(\/\w+(\.\w+)?)*(\/|\?\w*=\w*(&\w*=\w*)*)?[\"\'])*(>[a-zA-Z0-9 ="'<>.:;?]*</a>)
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"<a"+"href="0""*5000+"! _1_POA(i)"
 */
var REGEX = new RegExp("<a[a-zA-Z0-9 ="'.:;?]*(href=[\"\'](http:\/\/|\.\/|\/)?\w+(\.\w+)*(\/\w+(\.\w+)?)*(\/|\?\w*=\w*(&\w*=\w*)*)?[\"\'])*(>[a-zA-Z0-9 ="'<>.:;?]*</a>)")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '<a' + 'href=\"0\"'.repeat(i*10000) + '! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}