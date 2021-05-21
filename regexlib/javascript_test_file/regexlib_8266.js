/* 8266
 * ^(?i:([a-z0-9!#$%^&*{}'`+=-_|/?]+(?:\.[a-z0-9!#$%^&*{}'`+=-_|/?]+)*)@([a-z0-9]+\z?.*[a-z0-9-_]+)*(\.[a-z0-9]{2,}))$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"ia@"+"a"*16+"! _1SLQ_2"
 */
var REGEX = new RegExp("^(?i:([a-z0-9!#$%^&*{}'`+=-_|/?]+(?:\.[a-z0-9!#$%^&*{}'`+=-_|/?]+)*)@([a-z0-9]+\z?.*[a-z0-9-_]+)*(\.[a-z0-9]{2,}))$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'ia@' + 'a'.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}