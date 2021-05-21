# 8291
# ^[-+]?(\d?\d?\d?,?)?(\d{3}\,?)*(\.?\d+)$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"0"*5000+"!1 __POA(i)"

import re
from time import perf_counter

regex = """^[-+]?(\d?\d?\d?,?)?(\d{3}\,?)*(\.?\d+)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0" * i * 10000 + "!1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")