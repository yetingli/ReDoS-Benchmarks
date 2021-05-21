/* 2750
 * ^(?<From>(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|[ ]|,|/|[0-9])+)(-|–|:|TO)?(?<To>(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|[ ]|,|/|[0-9]|PRESENT)+)+(:)*
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"JUNE "*16+"! _1_EOD(i2)"
 */
var REGEX = new RegExp("^(?<From>(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|[ ]|,|/|[0-9])+)(-|–|:|TO)?(?<To>(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER|[ ]|,|/|[0-9]|PRESENT)+)+(:)*")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'JUNE '.repeat(i*1) + '! _1_EOD(i2)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}