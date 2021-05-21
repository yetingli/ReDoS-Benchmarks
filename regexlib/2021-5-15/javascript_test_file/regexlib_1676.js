/* 1676
 * (/\*[\d\D]*?\*/)|(\/\*(\s*|.*?)*\*\/)|(\/\/.*)|(/\\*[\\d\\D]*?\\*/)|([\r\n ]*//[^\r\n]*)+
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"/**//**///"+"/"*8+"!1 _SLQ_2"
 */
var REGEX = new RegExp("(/\*[\d\D]*?\*/)|(\/\*(\s*|.*?)*\*\/)|(\/\/.*)|(/\\*[\\d\\D]*?\\*/)|([\r\n ]*//[^\r\n]*)+")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '/**//**///' + '/'.repeat(i*1) + '!1 _SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}