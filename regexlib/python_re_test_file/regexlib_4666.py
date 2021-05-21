# 4666
# ([oO0]*)([|:;=X^])([-']*)([)(oO0\]\[DPp*>X^@])
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"o"*10000+"!1 _SLQ_1"

import re
from time import perf_counter

regex = """([oO0]*)([|:;=X^])([-']*)([)(oO0\]\[DPp*>X^@])"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "o" * i * 10000 + "!1 _SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")