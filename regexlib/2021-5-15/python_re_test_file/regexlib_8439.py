# 8439
# ^([a-zA-Z]\:|\\)\\([^\\]+\\)*[^\/:*?"<>|]+\.htm(l)?$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"a:\\"+"!\\"*5000+"!1 __POA(i)"

import re
from time import perf_counter

regex = """^([a-zA-Z]\:|\\)\\([^\\]+\\)*[^\/:*?"<>|]+\.htm(l)?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "a:\\" + "!\\" * i * 10000 + "!1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")