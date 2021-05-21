/* 3279
 * href\s*=\s*\"((\/)([i])(\/)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#]+)*)\"
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"href="/i/"+"1"*16+"! _1_NQ"
 */
var REGEX = new RegExp("href\s*=\s*\"((\/)([i])(\/)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#]+)*)\"")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'href=\"/i/' + '1'.repeat(i*1) + '! _1_NQ'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}