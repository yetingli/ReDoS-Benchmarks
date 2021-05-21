/* 5846
 * ((http|ftp|https|ftps):\/\/)?[\w\-_\.]+\.(([0-9]{1,3})|([a-zA-Z]{2,3})|(aero|arpa|asia|coop|info|jobs|mobi|museum|name|travel))+(:[0-9]+)?\/?(([\w\-\.,@^%:/~\+#]*[\w\-\@^%/~\+#])((\?[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*=[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*)+(&[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*=[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*)*)?)?
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"1.aaa"+"aa"*32+"! _1_NQ"
 */
var REGEX = new RegExp("((http|ftp|https|ftps):\/\/)?[\w\-_\.]+\.(([0-9]{1,3})|([a-zA-Z]{2,3})|(aero|arpa|asia|coop|info|jobs|mobi|museum|name|travel))+(:[0-9]+)?\/?(([\w\-\.,@^%:/~\+#]*[\w\-\@^%/~\+#])((\?[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*=[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*)+(&[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*=[a-zA-Z0-9\[\]\-\._+%\$#\=~',]*)*)?)?")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '1.aaa' + 'aa'.repeat(i*1) + '! _1_NQ'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}