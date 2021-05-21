/* 3451
 * <style.*?>(?<StyledText>.*)<\s*?/\s*?style.*?>
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"<style>"*512+"! _1SLQ_2"
 */
var REGEX = new RegExp("<style.*?>(?<StyledText>.*)<\s*?/\s*?style.*?>")
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '<style>'.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}