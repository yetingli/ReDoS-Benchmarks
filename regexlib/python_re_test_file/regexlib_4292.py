# 4292
# &lt;!--[\w\W]*?--&gt;
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"&lt;!--"*5000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """&lt;!--[\w\W]*?--&gt;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "&lt;!--" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")