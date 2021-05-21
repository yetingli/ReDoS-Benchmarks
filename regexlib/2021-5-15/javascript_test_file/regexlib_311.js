/* 311
 * (?<Code>[\s\S]*?)(?<NonCode>'.*?\r?\n|(?<quot>"|')(?:(?:(?!\<quot>).|\<quot>{2})*)(?:\<quot>))
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"""*5000+"! _1_POA(i)"
 */
var REGEX = /(?<Code>[\s\S]*?)(?<NonCode>'.*?\r?\n|(?<quot>"|')(?:(?:(?!\<quot>).|\<quot>{2})*)(?:\<quot>))/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '\"'.repeat(i*10000) + '! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}