/* 121
 * <a\s{1}href="(?<url>.*?)"(\s?target="(?<target>_(blank|new|parent|self|top))")?(\s?class="(?<class>.*?)")?(\s?style="(?<style>.*?)")?>(?<title>.*?)</a>
 * POLYNOMIAL
 * nums:3
 * POLYNOMIAL AttackString:"<a href="""+"class=""*5000+"! _1SLQ_2"
 */
var REGEX = new RegExp("<a\s{1}href="(?<url>.*?)"(\s?target="(?<target>_(blank|new|parent|self|top))")?(\s?class="(?<class>.*?)")?(\s?style="(?<style>.*?)")?>(?<title>.*?)</a>")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '<a href=\"\"' + 'class=\"'.repeat(i*10000) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 10000 + ": " + time_cost+" ms")
}