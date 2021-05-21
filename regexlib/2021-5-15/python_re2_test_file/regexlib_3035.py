# 3035
# (\d+(-\d+)*)+(,\d+(-\d+)*)*
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"1-1"*32+"! _1SLQ_1"

import re2 as re
from time import perf_counter

regex = """(\d+(-\d+)*)+(,\d+(-\d+)*)*"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1-1" * i * 1 + "! _1SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")