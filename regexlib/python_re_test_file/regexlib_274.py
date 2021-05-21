# 274
# ^[^\s]+@[^\.][^\s]{1,}\.[A-Za-z]{2,10}$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"@!!"*5000+"◎1 __POA(i)"

import re
from time import perf_counter

regex = """^[^\s]+@[^\.][^\s]{1,}\.[A-Za-z]{2,10}$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "@!!" * i * 10000 + "◎1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")