/* 4183
 * ^(?<scheme>(?:http|https|ftp|telnet|gopher|ms\-help|file|notes)://)?(?:(?<user>[a-z][\w~%!&amp;',;=\-\.$\(\)\*\+]*):(?<password>.*)?@)?(?:(?<domain>(?:[a-z0-9]\w*[a-z0-9]*\.)*(?:(?:(?:[a-z0-9]\w*[a-z0-9]*)(?:\.[a-z0-9]+)?)|(?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))))(?::(?<port>[0-9]+))?)?(?:(?<path>(?:/(?:[\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(?:%\d\d))+)*/(?:[\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(?:%\d\d))*)(?<params>\?[^#]+)?(?<fragment>#[a-z0-9]\w*)?)?$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"00."*32+"! _1_EOA(i or ii)"
 */
var REGEX = new RegExp("^(?<scheme>(?:http|https|ftp|telnet|gopher|ms\-help|file|notes)://)?(?:(?<user>[a-z][\w~%!&amp;',;=\-\.$\(\)\*\+]*):(?<password>.*)?@)?(?:(?<domain>(?:[a-z0-9]\w*[a-z0-9]*\.)*(?:(?:(?:[a-z0-9]\w*[a-z0-9]*)(?:\.[a-z0-9]+)?)|(?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))))(?::(?<port>[0-9]+))?)?(?:(?<path>(?:/(?:[\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(?:%\d\d))+)*/(?:[\w`~!$=;\-\+\.\^\(\)\|\{\}\[\]]|(?:%\d\d))*)(?<params>\?[^#]+)?(?<fragment>#[a-z0-9]\w*)?)?$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '00.'.repeat(i*1) + '! _1_EOA(i or ii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}