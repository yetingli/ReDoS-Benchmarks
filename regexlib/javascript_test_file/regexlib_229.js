/* 229
 * (\+1|1)?[ \-\.]?\(?(?<areacode>[0-9]{3})\)?[ \-\.]?(?<prefix>[0-9]{3})[ \-\.]?(?<number>[0-9]{4})[ \.]*(ext|x)?[ \.]*(?<extension>[0-9]{0,5})
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"0000000000"+" "*10000+"◎@! _1_POA(i)"
 */
var REGEX = /(\+1|1)?[ \-\.]?\(?(?<areacode>[0-9]{3})\)?[ \-\.]?(?<prefix>[0-9]{3})[ \-\.]?(?<number>[0-9]{4})[ \.]*(ext|x)?[ \.]*(?<extension>[0-9]{0,5})/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '0000000000' + ' '.repeat(i*10000) + '◎@! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}