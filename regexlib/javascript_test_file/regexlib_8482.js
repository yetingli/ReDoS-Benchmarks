/* 8482
 * ((MON|TUE|WED|THU|FRI|SAT|SUN)[A-Z]*)*[\ ,-]*(\d|\d{2})*(st|nd|rd|th)*[\ ,-]*(JAN|FEB|MAR|MAY|APR|JUL|JUN|AUG|OCT|SEP|NOV|DEC)[A-Z]*[\ ,]*(\d|\d{2}|\d{4})*(st|nd|rd|th)*([\ ,])*'*(\d{2}|\d{4})*\b
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:"JAN"+"00"*16+"! _1_EOD(i4)"
 */
var REGEX = /((MON|TUE|WED|THU|FRI|SAT|SUN)[A-Z]*)*[\ ,-]*(\d|\d{2})*(st|nd|rd|th)*[\ ,-]*(JAN|FEB|MAR|MAY|APR|JUL|JUN|AUG|OCT|SEP|NOV|DEC)[A-Z]*[\ ,]*(\d|\d{2}|\d{4})*(st|nd|rd|th)*([\ ,])*'*(\d{2}|\d{4})*\b/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = 'JAN' + '00'.repeat(i*1) + '! _1_EOD(i4)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}