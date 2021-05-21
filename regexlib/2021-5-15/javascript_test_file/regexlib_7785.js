/* 7785
 * ^([A-Z]|[a-z]|[0-9])([A-Z]|[a-z]|[0-9]|([A-Z]|[a-z]|[0-9]|(%|&|'|\+|\-|@|_|\.|\ )[^%&'\+\-@_\.\ ]|\.$|([%&'\+\-@_\.]\ [^\ ]|\ [%&'\+\-@_\.][^%&'\+\-@_\.])))+$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"A"+"A0"*16+"!1 __EOD(i1)"
 */
var REGEX = /^([A-Z]|[a-z]|[0-9])([A-Z]|[a-z]|[0-9]|([A-Z]|[a-z]|[0-9]|(%|&|'|\+|\-|@|_|\.|\ )[^%&'\+\-@_\.\ ]|\.$|([%&'\+\-@_\.]\ [^\ ]|\ [%&'\+\-@_\.][^%&'\+\-@_\.])))+$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'A' + 'A0'.repeat(i*1) + '!1 __EOD(i1)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}