/* 3450
 * <a.+?href\=(?<link>.+?)(?=[>\s]).*?>(?<lnkText>.+?)</a>
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"<a1href="*512+"! _1SLQ_2"
 */
var REGEX = new RegExp("<a.+?href\=(?<link>.+?)(?=[>\s]).*?>(?<lnkText>.+?)</a>")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '<a1href='.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}