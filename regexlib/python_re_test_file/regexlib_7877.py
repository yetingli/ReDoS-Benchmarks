# 7877
# &lt;a\s*.*?href\s*=\s*['&quot;](?!http:\/\/).*?&gt;(.*?)&lt;\/a&gt;
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"&lt;a"*10000+"!_1SLQ_2"

import re
from time import perf_counter

regex = """&lt;a\s*.*?href\s*=\s*['&quot;](?!http:\/\/).*?&gt;(.*?)&lt;\/a&gt;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "&lt;a" * i * 10000 + "!_1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")