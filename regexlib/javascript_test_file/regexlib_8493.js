/* 8493
 * ^(?<Date>.+\s\d+\s\d+\:\d+\:\d+).+\:.+\:(?<Traffic>.+)\:(?<Rule>.+)\:IN\=(?<InboundInterface>.+)\sOUT\=(?<OutboundIntercace>.*?)\s(?:MAC\=(?<MacAddress>.+)\s|)SRC\=(?<Source>.+)\sDST\=(?<Destination>.+)\sLEN\=.+TOS\=.+PROTO\=(?<Protocol>.+)\sSPT\=(?<SourcePort>.+)\sDPT\=(?<DestinationPort>.+)\s.+$
 * EXPONENT
 * nums:3
 * EXPONENT AttackString:""+"1 1 1:1:11:1:1:1:IN=1 OUT= SRC=1 DST=1 LEN=1TOS=1PROTO="*8+"! _1SLQ_2"
 */
var REGEX = /^(?<Date>.+\s\d+\s\d+\:\d+\:\d+).+\:.+\:(?<Traffic>.+)\:(?<Rule>.+)\:IN\=(?<InboundInterface>.+)\sOUT\=(?<OutboundIntercace>.*?)\s(?:MAC\=(?<MacAddress>.+)\s|)SRC\=(?<Source>.+)\sDST\=(?<Destination>.+)\sLEN\=.+TOS\=.+PROTO\=(?<Protocol>.+)\sSPT\=(?<SourcePort>.+)\sDPT\=(?<DestinationPort>.+)\s.+$/
for(var i = 1; i <= 5000000; i++) {
    var time = Date.now();
    var attack_str = '' + '1 1 1:1:11:1:1:1:IN=1 OUT= SRC=1 DST=1 LEN=1TOS=1PROTO='.repeat(i*1) + '! _1SLQ_2'
    REGEX.exec(attack_str)
    // REGEX.test(attack_str);
    // attack_str.search(REGEX)
    // attack_str.match(REGEX)
    var time_cost = Date.now() - time;
    console.log(i * 1 + ": " + time_cost+" ms")
}