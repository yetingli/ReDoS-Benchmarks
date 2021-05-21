/* 1611
 * ^(((h|H)(t|T))(t|T)(p|P)((s|S)?)\:\/\/)?((www|WWW)+\.)+(([0-9]{1,3}){3}[0-9]{1,3}\.|([\w!~*'()-]+\.)*([\w^-][\w-]{0,61})?[\w]\.[a-z]{2,6})(:[0-9]{1,4})?((\/*)|(\/+[\w!~*'().;?:@&=+$,%#-]+)+\/*)$
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"WWW."*5000+"! _1_POA(i)"
 */
var REGEX = new RegExp("^(((h|H)(t|T))(t|T)(p|P)((s|S)?)\:\/\/)?((www|WWW)+\.)+(([0-9]{1,3}){3}[0-9]{1,3}\.|([\w!~*'()-]+\.)*([\w^-][\w-]{0,61})?[\w]\.[a-z]{2,6})(:[0-9]{1,4})?((\/*)|(\/+[\w!~*'().;?:@&=+$,%#-]+)+\/*)$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'WWW.'.repeat(i*10000) + '! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}