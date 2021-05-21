# 4287
# ^((?:.*(?!\d))*(?:\D*)?)(\d+)$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"!"*5000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """^((?:.*(?!\d))*(?:\D*)?)(\d+)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "!" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")