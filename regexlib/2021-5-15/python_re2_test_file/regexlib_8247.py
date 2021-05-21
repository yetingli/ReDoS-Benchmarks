# 8247
# ^[a-z\.]*\s?([a-z\-\']+\s)+[a-z\-\']+$
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"a"*10000+"!1 __POA(i)"

import re2 as re
from time import perf_counter

regex = """^[a-z\.]*\s?([a-z\-\']+\s)+[a-z\-\']+$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "a" * i * 10000 + "!1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")