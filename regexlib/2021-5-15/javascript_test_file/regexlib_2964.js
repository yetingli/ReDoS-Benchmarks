/* 2964
 * (?:(?<scheme>[a-zA-Z]+)://)?(?<domain>(?:[0-9a-zA-Z\-_]+(?:[.][0-9a-zA-Z\-_]+)*))(?::(?<port>[0-9]+))?(?<path>(?:/[0-9a-zA-Z\-_.]+)+)(?:[?](?<query>.+))?
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"A"*5000+"!1 __POA(i)"
 */
var REGEX = new RegExp("(?:(?<scheme>[a-zA-Z]+)://)?(?<domain>(?:[0-9a-zA-Z\-_]+(?:[.][0-9a-zA-Z\-_]+)*))(?::(?<port>[0-9]+))?(?<path>(?:/[0-9a-zA-Z\-_.]+)+)(?:[?](?<query>.+))?")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'A'.repeat(i*10000) + '!1 __POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}