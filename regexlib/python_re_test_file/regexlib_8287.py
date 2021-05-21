# 8287
# ^[a-z0-9_.-]*@[a-z0-9-]+(.[a-z]{2,4})+$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"@"+"aaa"*5000+"!1 __POA(i)"

import re
from time import perf_counter

regex = """^[a-z0-9_.-]*@[a-z0-9-]+(.[a-z]{2,4})+$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "@" + "aaa" * i * 10000 + "!1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")