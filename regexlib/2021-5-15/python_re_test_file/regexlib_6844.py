# 6844
# [ ]*=[ ]*[\&quot;]*cid[ ]*:[ ]*([^\&quot;&lt;&gt; ]+)
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+" "*20000+"! _1SLQ_1q"

import re
from time import perf_counter

regex = """[ ]*=[ ]*[\&quot;]*cid[ ]*:[ ]*([^\&quot;&lt;&gt; ]+)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + " " * i * 10000 + "! _1SLQ_1q"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")