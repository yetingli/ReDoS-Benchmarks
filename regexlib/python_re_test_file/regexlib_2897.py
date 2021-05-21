# 2897
# ('.*$|Rem((\t| ).*$|$)|&quot;(.|&quot;&quot;)*?&quot;)
# EXPONENT
# nums:4
# EXPONENT AttackString:"&quot;"+"&quot;"*32+"! _1_EOA(iv)"

import re
from time import perf_counter

regex = """('.*$|Rem((\t| ).*$|$)|&quot;(.|&quot;&quot;)*?&quot;)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "&quot;" + "&quot;" * i * 1 + "! _1_EOA(iv)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")