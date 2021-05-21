/* 7093
 * ^(?<Namespace>(?:[\w][\w\d]*\.?)*)\.(?<Class>[\w][\w\d<>]*(?:(?:\+[\w][\w\d<>]*)+|))(?:|,\W?(?<Assembly>(?<AssemblyName>[^\W/\\:*?"<>|]+)(?:$|(?:,\W?(?:(?<Version>Version=(?<VersionValue>(?:\d{1,2}\.?){1,4}))|(?<Culture>Culture=(?<CultureValue>neutral|\w{2}-\w{2}))|(?<PublicKeyToken>PublicKeyToken=(?<PublicKeyTokenValue>[A-Fa-f0-9]{16})))(?:,\W?)?){3})))$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"0"*32+"!1 __EOA(iii)"
 */
var REGEX = new RegExp("^(?<Namespace>(?:[\w][\w\d]*\.?)*)\.(?<Class>[\w][\w\d<>]*(?:(?:\+[\w][\w\d<>]*)+|))(?:|,\W?(?<Assembly>(?<AssemblyName>[^\W/\\:*?"<>|]+)(?:$|(?:,\W?(?:(?<Version>Version=(?<VersionValue>(?:\d{1,2}\.?){1,4}))|(?<Culture>Culture=(?<CultureValue>neutral|\w{2}-\w{2}))|(?<PublicKeyToken>PublicKeyToken=(?<PublicKeyTokenValue>[A-Fa-f0-9]{16})))(?:,\W?)?){3})))$")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '0'.repeat(i*1) + '!1 __EOA(iii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}