/* 1618
 * ^\s*(?<Last>[-A-Za-z ]+)[.](?<First>[-A-Za-z ]+)(?:[.](?<Middle>[-A-Za-z ]+))?(?:[.](?<Ordinal>[IVX]+))?(?:[.](?<Number>\d{10}))\s*$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+" "*10000+"!_1_POA(i)"
 */
var REGEX = /^\s*(?<Last>[-A-Za-z ]+)[.](?<First>[-A-Za-z ]+)(?:[.](?<Middle>[-A-Za-z ]+))?(?:[.](?<Ordinal>[IVX]+))?(?:[.](?<Number>\d{10}))\s*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + ' '.repeat(i*10000) + '!_1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}