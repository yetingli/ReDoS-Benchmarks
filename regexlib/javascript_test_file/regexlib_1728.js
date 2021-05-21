/* 1728
 * (".+"\s)?<?[a-z\._0-9]+[^\._]@([a-z0-9]+\.)+[a-z0-9]{2,6}>?;?
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"""*10000+"! _1SLQ_2"
 */
var REGEX = /(".+"\s)?<?[a-z\._0-9]+[^\._]@([a-z0-9]+\.)+[a-z0-9]{2,6}>?;?/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '\"'.repeat(i*10000) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}