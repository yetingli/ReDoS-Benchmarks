/* 3821
 * ^\s*([A-Za-z]{2,4}\.?\s*)?(['\-A-Za-z]+\s*){1,2}([A-Za-z]+\.?\s*)?(['\-A-Za-z]+\s*){1,2}(([jJsSrR]{2}\.)|([XIV]{1,6}))?\s*$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"AA"*32+"!_1SLQ_2"
 */
var REGEX = /^\s*([A-Za-z]{2,4}\.?\s*)?(['\-A-Za-z]+\s*){1,2}([A-Za-z]+\.?\s*)?(['\-A-Za-z]+\s*){1,2}(([jJsSrR]{2}\.)|([XIV]{1,6}))?\s*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'AA'.repeat(i*1) + '!_1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}