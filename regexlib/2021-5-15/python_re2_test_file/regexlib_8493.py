# 8493
# ^(?<Date>.+\s\d+\s\d+\:\d+\:\d+).+\:.+\:(?<Traffic>.+)\:(?<Rule>.+)\:IN\=(?<InboundInterface>.+)\sOUT\=(?<OutboundIntercace>.*?)\s(?:MAC\=(?<MacAddress>.+)\s|)SRC\=(?<Source>.+)\sDST\=(?<Destination>.+)\sLEN\=.+TOS\=.+PROTO\=(?<Protocol>.+)\sSPT\=(?<SourcePort>.+)\sDPT\=(?<DestinationPort>.+)\s.+$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"1 1 1:1:11:1:1:1:IN=1 OUT= SRC=1 DST=1 LEN=1TOS=1PROTO="*8+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """^(?<Date>.+\s\d+\s\d+\:\d+\:\d+).+\:.+\:(?<Traffic>.+)\:(?<Rule>.+)\:IN\=(?<InboundInterface>.+)\sOUT\=(?<OutboundIntercace>.*?)\s(?:MAC\=(?<MacAddress>.+)\s|)SRC\=(?<Source>.+)\sDST\=(?<Destination>.+)\sLEN\=.+TOS\=.+PROTO\=(?<Protocol>.+)\sSPT\=(?<SourcePort>.+)\sDPT\=(?<DestinationPort>.+)\s.+$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1 1 1:1:11:1:1:1:IN=1 OUT= SRC=1 DST=1 LEN=1TOS=1PROTO=" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")