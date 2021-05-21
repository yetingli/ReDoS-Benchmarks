/* 3764
 * (?=^.{1,160}$)^(?:(((?:([a-zA-Z]\:)|(\\{2}[a-zA-Z]\w*)))((?:\\((?:(?![\w\.]*\.(?:gdb|mdb|sde|mdf))[^\\/:*?<>"| .]+[^\\/:*?<>"|]*[^\\/:*?<>"| .]+)))*)(?:\\(([a-zA-Z]\w*)(\.(?:gdb|mdb|sde|mdf))))?)\\?([a-zA-Z]\w*)?(?:\\([a-zA-Z]\w*(?:\.shp)?)(?<!.+(?:\.(?:gdb|mdb|sde|mdf)).+\.shp|(?<!.+(?:\.(?:gdb|mdb|sde|mdf)).+)(?<!.+\.shp))))$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"a:"+"\\!!!"*16+"! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("(?=^.{1,160}$)^(?:(((?:([a-zA-Z]\:)|(\\{2}[a-zA-Z]\w*)))((?:\\((?:(?![\w\.]*\.(?:gdb|mdb|sde|mdf))[^\\/:*?<>"| .]+[^\\/:*?<>"|]*[^\\/:*?<>"| .]+)))*)(?:\\(([a-zA-Z]\w*)(\.(?:gdb|mdb|sde|mdf))))?)\\?([a-zA-Z]\w*)?(?:\\([a-zA-Z]\w*(?:\.shp)?)(?<!.+(?:\.(?:gdb|mdb|sde|mdf)).+\.shp|(?<!.+(?:\.(?:gdb|mdb|sde|mdf)).+)(?<!.+\.shp))))$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'a:' + '\\!!!'.repeat(i*1) + '! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}