# 3759
# (?<prefix>[\d]{3})[\s+\/\\\-]+(?<number>[\d\-\s]+)
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"111"+"\t"*10000+"!1 __POA(i)"

import re2 as re
from time import perf_counter

regex = """(?<prefix>[\d]{3})[\s+\/\\\-]+(?<number>[\d\-\s]+)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "111" + "\t" * i * 10000 + "!1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")