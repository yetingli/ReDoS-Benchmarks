/* 2763
 * [0-9]+[stndrh]*\s*(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s*([0-9][0-9][0-9][0-9])?|(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s*[0-9]+[stndrh]*|[0-9]+[\/.-][0-9]+[\/.-][0-9]+[0-9]+|[saturnmoewdhfi]*day
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:""+"s"*20000+"! _1SLQ_1"
 */
var REGEX = new RegExp("[0-9]+[stndrh]*\s*(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s*([0-9][0-9][0-9][0-9])?|(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s*[0-9]+[stndrh]*|[0-9]+[\/.-][0-9]+[\/.-][0-9]+[0-9]+|[saturnmoewdhfi]*day")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 's'.repeat(i*10000) + '! _1SLQ_1'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}