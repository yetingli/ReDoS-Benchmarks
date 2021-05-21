/* 8366
 * (?<STag><)[/\?\s]*(?<Prefix>\w*:)*(?<TagName>\w*)\s*(?<Attributes>(?<Attribute>((?<AttributePrefix>\w*)\s*:\s*)*(?<AttributeName>\w*)\s*=\s*(?<AttributeValue>"[^"]*"|'[^']*'|[^>\s]*)\s*)*)\s*/?(?<ETag>>)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"<"+"\t=:''"*32+"! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("(?<STag><)[/\?\s]*(?<Prefix>\w*:)*(?<TagName>\w*)\s*(?<Attributes>(?<Attribute>((?<AttributePrefix>\w*)\s*:\s*)*(?<AttributeName>\w*)\s*=\s*(?<AttributeValue>"[^"]*"|'[^']*'|[^>\s]*)\s*)*)\s*/?(?<ETag>>)")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '<' + '\t=:\'\''.repeat(i*1) + '! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}