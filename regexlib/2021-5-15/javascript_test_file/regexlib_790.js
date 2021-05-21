/* 790
 * (SELECT\s[\w\*\)\(\,\s]+\sFROM\s[\w]+)|(UPDATE\s[\w]+\sSET\s[\w\,\'\=]+)|(INSERT\sINTO\s[\d\w]+[\s\w\d\)\(\,]*\sVALUES\s\([\d\w\'\,\)]+)|(DELETE\sFROM\s[\d\w\'\=]+)
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"SELECT "*5000+"!1 _SLQ_2"
 */
var REGEX = /(SELECT\s[\w\*\)\(\,\s]+\sFROM\s[\w]+)|(UPDATE\s[\w]+\sSET\s[\w\,\'\=]+)|(INSERT\sINTO\s[\d\w]+[\s\w\d\)\(\,]*\sVALUES\s\([\d\w\'\,\)]+)|(DELETE\sFROM\s[\d\w\'\=]+)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'SELECT '.repeat(i*10000) + '!1 _SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}