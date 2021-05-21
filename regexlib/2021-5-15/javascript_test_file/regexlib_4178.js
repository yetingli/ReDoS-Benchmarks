/* 4178
 * ^(?:mailto:)?(?:[a-z][\w~%!&amp;',;=\-\.$\(\)\*\+]*)@(?:[a-z0-9][\w\-]*[a-z0-9]*\.)*(?:(?:(?:[a-z0-9][\w\-]*[a-z0-9]*)(?:\.[a-z0-9]+)?)|(?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)))$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"a@250.250.250."+"000"*256+"! _1_EOA(iii)"
 */
var REGEX = /^(?:mailto:)?(?:[a-z][\w~%!&amp;',;=\-\.$\(\)\*\+]*)@(?:[a-z0-9][\w\-]*[a-z0-9]*\.)*(?:(?:(?:[a-z0-9][\w\-]*[a-z0-9]*)(?:\.[a-z0-9]+)?)|(?:(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)))$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'a@250.250.250.' + '000'.repeat(i*1) + '! _1_EOA(iii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}