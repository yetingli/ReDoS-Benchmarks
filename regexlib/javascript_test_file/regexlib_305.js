/* 305
 * (?<=(?:\n|:|^)\s*?)(if|end\sif|elseif|else|for\seach|for|next|call|class|exit|do|loop|const|dim|erase|option\s(?:explicit|implicit)|(?:public|private|end)\ssub|(?:public|private|end)\sfunction|private|public|redim|select\scase|end\sselect|case\selse|case|set|while|wend|with|end\swith|on\serror\sgoto\s0|on\serror\sresume\snext|exit|end\sclass|property\slet|property\sget|property\sset)(?=\s|$)
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"<="+"\n"*5000+"!_1SLQ_2"
 */
var REGEX = /(?<=(?:\n|:|^)\s*?)(if|end\sif|elseif|else|for\seach|for|next|call|class|exit|do|loop|const|dim|erase|option\s(?:explicit|implicit)|(?:public|private|end)\ssub|(?:public|private|end)\sfunction|private|public|redim|select\scase|end\sselect|case\selse|case|set|while|wend|with|end\swith|on\serror\sgoto\s0|on\serror\sresume\snext|exit|end\sclass|property\slet|property\sget|property\sset)(?=\s|$)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '<=' + '\n'.repeat(i*10000) + '!_1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}