/* 306
 * (?<=(?:\n|:|&|\()\s*?)(Application\.Unlock|Application\.Lock|Application\.Contents\.RemoveAll|Application\.Contents\.Remove|Request\.BinaryRead|Request\.ClientCertificate|Request\.Cookies|Request\.Form|Request\.QueryString|Request\.ServerVariables|Request\.TotalBytes|Response\.AddHeader|Response\.AppendToLog|Response\.BinaryWrite|Response\.Clear|Response\.End|Response\.Flush|Response\.Redirect|Response\.Write|Response\.Buffer|Response\.CacheControl|Response\.Charset|Response\.CodePage|Response\.ContentType|Response\.Cookies|Response\.Expires|Response\.ExpiresAbsolute|Response\.IsClientConnected|Response\.LCID|Response\.PICS|Response\.Status|Server\.ScriptTimeout|Server\.CreateObject|Server\.Execute|Server\.GetLastError|Server\.HTMLEncode|Server\.MapPath|Server\.Transfer|Server\.URLEncode|Session\.Abandon|Session\.Contents\.Remove|Session\.Contents\.RemoveAll|Session\.CodePage|Session\.Contents|Session\.LCID|Session\.SessionID|Session\.StaticObjects|Session\.Timeout|Application|Session|Request)(?=\s|\.|\()
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"<="+"\n"*10000+"!_1SLQ_2"
 */
var REGEX = /(?<=(?:\n|:|&|\()\s*?)(Application\.Unlock|Application\.Lock|Application\.Contents\.RemoveAll|Application\.Contents\.Remove|Request\.BinaryRead|Request\.ClientCertificate|Request\.Cookies|Request\.Form|Request\.QueryString|Request\.ServerVariables|Request\.TotalBytes|Response\.AddHeader|Response\.AppendToLog|Response\.BinaryWrite|Response\.Clear|Response\.End|Response\.Flush|Response\.Redirect|Response\.Write|Response\.Buffer|Response\.CacheControl|Response\.Charset|Response\.CodePage|Response\.ContentType|Response\.Cookies|Response\.Expires|Response\.ExpiresAbsolute|Response\.IsClientConnected|Response\.LCID|Response\.PICS|Response\.Status|Server\.ScriptTimeout|Server\.CreateObject|Server\.Execute|Server\.GetLastError|Server\.HTMLEncode|Server\.MapPath|Server\.Transfer|Server\.URLEncode|Session\.Abandon|Session\.Contents\.Remove|Session\.Contents\.RemoveAll|Session\.CodePage|Session\.Contents|Session\.LCID|Session\.SessionID|Session\.StaticObjects|Session\.Timeout|Application|Session|Request)(?=\s|\.|\()/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '<=' + '\n'.repeat(i*10000) + '!_1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}