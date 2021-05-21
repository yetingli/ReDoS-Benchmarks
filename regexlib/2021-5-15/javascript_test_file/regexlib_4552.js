/* 4552
 * (^[A-ZÀ-Ü]{1}[a-zà-ü']+\s[a-zA-Zà-üÀ-Ü]+((([\s\.'])|([a-zà-ü']+))|[a-zà-ü']+[a-zA-Zà-üÀ-Ü']+))
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"Aa "+"a"*5000+"!1 __POA(i)"
 */
var REGEX = /(^[A-ZÀ-Ü]{1}[a-zà-ü']+\s[a-zA-Zà-üÀ-Ü]+((([\s\.'])|([a-zà-ü']+))|[a-zà-ü']+[a-zA-Zà-üÀ-Ü']+))/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'Aa ' + 'a'.repeat(i*10000) + '!1 __POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}