# 4387
# ([a-zA-Z0-9\\-\\$\\s\\.#@%^*(){}|:;,?+=/]*[<>'\"!&\\[\\]]+((\\s|)CDATA(\\s|))*[a-zA-Z0-9<>'\"!&\\[\\]\\-\\$\\s\\.#@%^*(){}|:;,?+=/]*)+
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"<"*16+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """([a-zA-Z0-9\\-\\$\\s\\.#@%^*(){}|:;,?+=/]*[<>'\"!&\\[\\]]+((\\s|)CDATA(\\s|))*[a-zA-Z0-9<>'\"!&\\[\\]\\-\\$\\s\\.#@%^*(){}|:;,?+=/]*)+"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "<" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")