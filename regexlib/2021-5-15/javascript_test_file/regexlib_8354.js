/* 8354
 * (http|https)\:\/\/(([\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3})|([\w\-]+\.)+(((af|ax|al|dz|as|ad|ao|ai|aq|ag|am|aw|au|at|az|bs|bh|bd|bb|by|be|bz|bj|bm|bt|bo|ba|bw|bv|br|io|bn|bg|bf|kh|cm|ca|cv|ky|cf|td|cl|cn|cx|cc|km|cg|cd|ck|cr|ci|hr|cu|cy|cz|dk|dj|dm|do|ec|eg|sv|gq|er|ee|et|fk|fo|fj|fi|fr|gf|pf|tf|ga|gm|ge|de|gh|gi|gr|gl|gd|gp|gu|gt| gg|gn|gw|gy|ht|hm|va|hn|hk|hu|is|id|ir|iq|ie|im|il|it|jm|jp|je|jo|kz|ke|ki|kp|kr|kw|kg|la|lv|lb|ls|lr|ly|li|lt|lu|mo|mk|mg|mw|my|mv|ml|mt|mh|mq|mr|yt|mx|fm|md|mc|mn|ms|ma|mz|mm|nr|np|nl|an|nc|nz|ni|ng|nu|nf|mp|no|om|pk|pw|ps|pa|pg|py|pe|ph|pn|pl|pt|qa|re|ro|ru|rw|sh|kn|lc|pm|vc|ws|sm|st|sa|sn|cs|sc|sl|sg|sk|si|sb|so|za|gs|es|lk|sd|sr|sj|sz|se|ch|sy|tw|tj|tz|th|tl|tg|tk|to|tt|tn|tr|tm|tc|tv|ug|ua|gb|us|um|uy|uz|vu|ve|vn|vg|vi|wf|eh|ye|zm|zw|uk|com|edu|gov|int|mil|net|org|biz|info|name|pro|aero|coop|museum|arpa|co|in|ne|bi|na|pr|ae|mu|ar))))(:[\d]{1,4})?($|(\/([a-zA-Z0-9\.\?=/#%&\+-])*)*|\/)
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"http://1.1.1.1"+"/"*32+"! _1_EOA(iii)"
 */
var REGEX = new RegExp("(http|https)\:\/\/(([\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3})|([\w\-]+\.)+(((af|ax|al|dz|as|ad|ao|ai|aq|ag|am|aw|au|at|az|bs|bh|bd|bb|by|be|bz|bj|bm|bt|bo|ba|bw|bv|br|io|bn|bg|bf|kh|cm|ca|cv|ky|cf|td|cl|cn|cx|cc|km|cg|cd|ck|cr|ci|hr|cu|cy|cz|dk|dj|dm|do|ec|eg|sv|gq|er|ee|et|fk|fo|fj|fi|fr|gf|pf|tf|ga|gm|ge|de|gh|gi|gr|gl|gd|gp|gu|gt| gg|gn|gw|gy|ht|hm|va|hn|hk|hu|is|id|ir|iq|ie|im|il|it|jm|jp|je|jo|kz|ke|ki|kp|kr|kw|kg|la|lv|lb|ls|lr|ly|li|lt|lu|mo|mk|mg|mw|my|mv|ml|mt|mh|mq|mr|yt|mx|fm|md|mc|mn|ms|ma|mz|mm|nr|np|nl|an|nc|nz|ni|ng|nu|nf|mp|no|om|pk|pw|ps|pa|pg|py|pe|ph|pn|pl|pt|qa|re|ro|ru|rw|sh|kn|lc|pm|vc|ws|sm|st|sa|sn|cs|sc|sl|sg|sk|si|sb|so|za|gs|es|lk|sd|sr|sj|sz|se|ch|sy|tw|tj|tz|th|tl|tg|tk|to|tt|tn|tr|tm|tc|tv|ug|ua|gb|us|um|uy|uz|vu|ve|vn|vg|vi|wf|eh|ye|zm|zw|uk|com|edu|gov|int|mil|net|org|biz|info|name|pro|aero|coop|museum|arpa|co|in|ne|bi|na|pr|ae|mu|ar))))(:[\d]{1,4})?($|(\/([a-zA-Z0-9\.\?=/#%&\+-])*)*|\/)")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'http://1.1.1.1' + '/'.repeat(i*1) + '! _1_EOA(iii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}