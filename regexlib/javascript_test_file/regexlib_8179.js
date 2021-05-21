/* 8179
 * <a.*?href=[""'](?<uri>(?<path>.*?)file:(?<file>.*?))[""'].*?>(?<description>.*?)</a>
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"<ahref="file:">"*32+"! _1SLQ_2"
 */
var REGEX = new RegExp("<a.*?href=[""'](?<uri>(?<path>.*?)file:(?<file>.*?))[""'].*?>(?<description>.*?)</a>")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '<ahref=\"file:\">'.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}