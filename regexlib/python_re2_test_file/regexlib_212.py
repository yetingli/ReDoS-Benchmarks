# 212
# ^[\n &lt;&quot;']*([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+)
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"l"*10000+"!1 __POA(i)"

import re2 as re
from time import perf_counter

regex = """^[\n &lt;&quot;']*([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "l" * i * 10000 + "!1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")