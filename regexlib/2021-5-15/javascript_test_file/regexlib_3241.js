/* 3241
 * <[iI][mM][gG][a-zA-Z0-9\s=".]*((src)=\s*(?:"([^"]*)"|'[^']*'))[a-zA-Z0-9\s=".]*/*>(?:</[iI][mM][gG]>)*
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"<img"+"src="""*5000+"! _1_POA(i)"
 */
var REGEX = new RegExp("<[iI][mM][gG][a-zA-Z0-9\s=".]*((src)=\s*(?:"([^"]*)"|'[^']*'))[a-zA-Z0-9\s=".]*/*>(?:</[iI][mM][gG]>)*")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '<img' + 'src=\"\"'.repeat(i*10000) + '! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}