/* 2403
 * actionID=&url=&load_frameset=1&autologin=0&anchor_string=&server_key=imap&imapuser=(.*)&pass=(.*)&new_lang=pt_BR&select_view=imp
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"actionID=&url=&load_frameset=1&autologin=0&anchor_string=&server_key=imap&imapuser=&pass="*256+"! _1SLQ_2"
 */
var REGEX = /actionID=&url=&load_frameset=1&autologin=0&anchor_string=&server_key=imap&imapuser=(.*)&pass=(.*)&new_lang=pt_BR&select_view=imp/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'actionID=&url=&load_frameset=1&autologin=0&anchor_string=&server_key=imap&imapuser=&pass='.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}