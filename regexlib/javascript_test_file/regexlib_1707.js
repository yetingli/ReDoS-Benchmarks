/* 1707
 * (<log4j:Event logger=")(.*?)(" timestamp=")(.*?)(" level=")(.*?)(" thread=")(.*?)(">)(.*?)(<log4j:Message><!\[CDATA\[)(.*?)(\]\]>)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"<log4j:Event logger="" timestamp="" level="" thread=""*64+"! _1SLQ_2"
 */
var REGEX = /(<log4j:Event logger=")(.*?)(" timestamp=")(.*?)(" level=")(.*?)(" thread=")(.*?)(">)(.*?)(<log4j:Message><!\[CDATA\[)(.*?)(\]\]>)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '<log4j:Event logger=\"\" timestamp=\"\" level=\"\" thread=\"'.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}