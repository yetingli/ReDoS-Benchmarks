/* 1694
 * ((A[FGIKLMNPRSUZ]S?X?|DAL?L?A?E?S?|DE|DE[LNRST]L?A?E?H?I?O?S?|DI[AE]?|DOS?|DU|EIT?N?E?|ELS?|EN|ETT?|HAI?|HE[NT]|HIN?A?I?N?R?|HOI|IL|IM|ISA|KA|KE|LAS|LES?|LH?IS?|LOS?|LO?U|MA?C|N[AIY]|O[IP]|SI|T[AEO]N?R?|U[MN][AEOS]?|VAN|VE[LR]|VO[MN]|Y[ENR]|ZU[MR]?) )?((LAS?|LOS?|DEN?R?|ZU) )?[A-Z0/'\.-]+( |$)(SR|JR|II+V?|VI+|[1-9][STRDH]+)?
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"II"*5000+"! _1_POA(i)"
 */
var REGEX = new RegExp("((A[FGIKLMNPRSUZ]S?X?|DAL?L?A?E?S?|DE|DE[LNRST]L?A?E?H?I?O?S?|DI[AE]?|DOS?|DU|EIT?N?E?|ELS?|EN|ETT?|HAI?|HE[NT]|HIN?A?I?N?R?|HOI|IL|IM|ISA|KA|KE|LAS|LES?|LH?IS?|LOS?|LO?U|MA?C|N[AIY]|O[IP]|SI|T[AEO]N?R?|U[MN][AEOS]?|VAN|VE[LR]|VO[MN]|Y[ENR]|ZU[MR]?) )?((LAS?|LOS?|DEN?R?|ZU) )?[A-Z0/'\.-]+( |$)(SR|JR|II+V?|VI+|[1-9][STRDH]+)?")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'II'.repeat(i*10000) + '! _1_POA(i)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}