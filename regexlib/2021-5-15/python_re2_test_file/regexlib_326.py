# 326
# ^(?:(?<key>.+?)\s*?=\s*?(?<value>\S.+?)\s*)$
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"\t"*10000+"! _1_POA(i)"

import re2 as re
from time import perf_counter

regex = """^(?:(?<key>.+?)\s*?=\s*?(?<value>\S.+?)\s*)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "\t" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")