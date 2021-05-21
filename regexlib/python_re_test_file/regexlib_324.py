# 324
# ^\w+\W+(\w+)([a-z])(\w+)\s\&\s\w+\W+\1(?!\2)[a-z]\3$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"1:"+"a0"*5000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """^\w+\W+(\w+)([a-z])(\w+)\s\&\s\w+\W+\1(?!\2)[a-z]\3$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1:" + "a0" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")