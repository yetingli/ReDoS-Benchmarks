/* 7023
 * ^(ht|f)tp(s?)\:\/\/[a-zA-Z0-9\-\._]+(\.[a-zA-Z0-9\-\._]+){2,}(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]*)?$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"http://a.a.a"+"."*32+"! _1_EOA(iv)"
 */
var REGEX = new RegExp("^(ht|f)tp(s?)\:\/\/[a-zA-Z0-9\-\._]+(\.[a-zA-Z0-9\-\._]+){2,}(\/?)([a-zA-Z0-9\-\.\?\,\'\/\\\+&amp;%\$#_]*)?$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'http://a.a.a' + '.'.repeat(i*1) + '! _1_EOA(iv)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}