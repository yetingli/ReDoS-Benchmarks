/* 3434
 * \d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}\s.\s.\s\[\d{2}\/\D{3}\/\d{4}:\d{1,2}:\d{1,2}:\d{1,2}\s.\d{4}\]\s\&quot;\S*\s\S*\s\S*\&quot;\s\d{1,3}\s\S*\s\&quot;.*\&quot;\s\&quot;.*\&quot;
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"1.1.1.1 1 1 [11/:::/1111:1:1:1 11111] &quot;  &quot; 1  &quot;&quot; &quot;"*5000+"! _1SLQ_2"
 */
var REGEX = new RegExp("\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}\s.\s.\s\[\d{2}\/\D{3}\/\d{4}:\d{1,2}:\d{1,2}:\d{1,2}\s.\d{4}\]\s\&quot;\S*\s\S*\s\S*\&quot;\s\d{1,3}\s\S*\s\&quot;.*\&quot;\s\&quot;.*\&quot;")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '1.1.1.1 1 1 [11/:::/1111:1:1:1 11111] &quot;  &quot; 1  &quot;&quot; &quot;'.repeat(i*10000) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}