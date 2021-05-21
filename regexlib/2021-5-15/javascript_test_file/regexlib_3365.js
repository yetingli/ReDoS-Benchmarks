/* 3365
 * ([a-zA-Z1-9]*)\.(((a|A)(s|S)(p|P)(x|X))|((h|H)(T|t)(m|M)(l|L))|((h|H)(t|T)(M|m))|((a|A)(s|S)(p|P))|((t|T)(x|X)(T|x))|((m|M)(S|s)(P|p)(x|X))|((g|G)(i|I)(F|f))|((d|D)(o|O)(c|C)))
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"a"*10000+"◎@! _1SLQ_1"
 */
var REGEX = /([a-zA-Z1-9]*)\.(((a|A)(s|S)(p|P)(x|X))|((h|H)(T|t)(m|M)(l|L))|((h|H)(t|T)(M|m))|((a|A)(s|S)(p|P))|((t|T)(x|X)(T|x))|((m|M)(S|s)(P|p)(x|X))|((g|G)(i|I)(F|f))|((d|D)(o|O)(c|C)))/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'a'.repeat(i*10000) + '◎@! _1SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}