/* 7935
 * (([\n,  ])*((<+)([^<>]+)(>*))+([\n,  ])*)+
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"\n< >\n"*16+"SLQ_1"
 */
var REGEX = /(([\n,  ])*((<+)([^<>]+)(>*))+([\n,  ])*)+/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '\n< >\n'.repeat(i*1) + 'SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}