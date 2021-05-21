/* 2073
 * (?<FirstName>[A-Z]\.?\w*\-?[A-Z]?\w*)\s?(?<MiddleName>[A-Z]\w+|[A-Z]?\.?)\s(?<LastName>[A-Z]?\w{0,3}[A-Z]\w+\-?[A-Z]?\w*)(?:,\s|)(?<Suffix>Jr\.|Sr\.|IV|III|II|)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"AA1 "+"A1"*512+"! _1SLQ_2"
 */
var REGEX = /(?<FirstName>[A-Z]\.?\w*\-?[A-Z]?\w*)\s?(?<MiddleName>[A-Z]\w+|[A-Z]?\.?)\s(?<LastName>[A-Z]?\w{0,3}[A-Z]\w+\-?[A-Z]?\w*)(?:,\s|)(?<Suffix>Jr\.|Sr\.|IV|III|II|)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'AA1 ' + 'A1'.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}