/* 4272
 * ^(((\.\.){1}/)*|(/){1})?(([a-zA-Z0-9]*)/)*([a-zA-Z0-9]*)+([.jpg]|[.gif])+$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"f"*32+"!1 _!\n_SLQ_3"
 */
var REGEX = new RegExp("^(((\.\.){1}/)*|(/){1})?(([a-zA-Z0-9]*)/)*([a-zA-Z0-9]*)+([.jpg]|[.gif])+$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'f'.repeat(i*1) + '!1 _!\n_SLQ_3'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}