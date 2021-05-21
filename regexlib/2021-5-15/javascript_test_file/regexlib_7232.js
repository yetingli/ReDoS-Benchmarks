/* 7232
 * (?:(?:(\d+)[ ]*(?:'|ft)){0,1}[ ]*(\d*(?![/\w])){0,1}(?:[ ,\-]){0,1}((\d*)\/(\d*)){0,1}(\.\d*){0,1}(?:\x22| in))|(?:(\d+)[ ]*(?:'|ft)[ ]*){1}
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"1"*5000+"!1 _SLQ_2"
 */
var REGEX = new RegExp("(?:(?:(\d+)[ ]*(?:'|ft)){0,1}[ ]*(\d*(?![/\w])){0,1}(?:[ ,\-]){0,1}((\d*)\/(\d*)){0,1}(\.\d*){0,1}(?:\x22| in))|(?:(\d+)[ ]*(?:'|ft)[ ]*){1}")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '1'.repeat(i*10000) + '!1 _SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}