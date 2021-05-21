/* 5850
 * (?<username>#?[+_a-zA-Z0-9+-]+(\.[+_a-zA-Z0-9+-]+)*)@(?<domain>[a-zA-Z0-9]+(-(?!-)|[a-zA-Z0-9\.])*?[a-zA-Z0-9]+\.([0-9]{1,3}|[a-zA-Z]{2,3}|(aero|arpa|asia|coop|info|jobs|mobi|museum|name|travel)))
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"+@a"+"B"*512+"! _1!\n_SLQ_3"
 */
var REGEX = /(?<username>#?[+_a-zA-Z0-9+-]+(\.[+_a-zA-Z0-9+-]+)*)@(?<domain>[a-zA-Z0-9]+(-(?!-)|[a-zA-Z0-9\.])*?[a-zA-Z0-9]+\.([0-9]{1,3}|[a-zA-Z]{2,3}|(aero|arpa|asia|coop|info|jobs|mobi|museum|name|travel)))/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '+@a' + 'B'.repeat(i*1) + '! _1!\n_SLQ_3'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}