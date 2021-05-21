# 3657
# &lt;[iI][mM][gG]([^&gt;]*[^/&gt;]*[/&gt;]*[&gt;])
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"&lt;img"+"!"*5000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """&lt;[iI][mM][gG]([^&gt;]*[^/&gt;]*[/&gt;]*[&gt;])"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "&lt;img" + "!" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")