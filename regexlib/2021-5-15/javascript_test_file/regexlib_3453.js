/* 3453
 * (?:(?<protocol>http(?:s?)|ftp)(?:\:\/\/))(?:(?<usrpwd>\w+\:\w+)(?:\@))?(?<domain>[^/\r\n\:]+)?(?<port>\:\d+)?(?<path>(?:\/.*)*\/)?(?<filename>.*?\.(?<ext>\w{2,4}))?(?<qrystr>\??(?:\w+\=[^\#]+)(?:\&?\w+\=\w+)*)*(?<bkmrk>\#.*)?
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"http://"+"/"*32+"! _1_EOA(iii)"
 */
var REGEX = new RegExp("(?:(?<protocol>http(?:s?)|ftp)(?:\:\/\/))(?:(?<usrpwd>\w+\:\w+)(?:\@))?(?<domain>[^/\r\n\:]+)?(?<port>\:\d+)?(?<path>(?:\/.*)*\/)?(?<filename>.*?\.(?<ext>\w{2,4}))?(?<qrystr>\??(?:\w+\=[^\#]+)(?:\&?\w+\=\w+)*)*(?<bkmrk>\#.*)?")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'http://' + '/'.repeat(i*1) + '! _1_EOA(iii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}