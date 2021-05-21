/* 1796
 * target[ ]*[=]([ ]*)([&quot;]|['])*([_])*([A-Za-z0-9])+([&quot;])*
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"target="+"o"*1024+"!1 _!1 _!1 _! _1!\n_SLQ_3"
 */
var REGEX = /target[ ]*[=]([ ]*)([&quot;]|['])*([_])*([A-Za-z0-9])+([&quot;])*/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'target=' + 'o'.repeat(i*1) + '!1 _!1 _!1 _! _1!\n_SLQ_3'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}