# 5511
# ^([a-z]+?\.[a-z]+)+\%$
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"aaa."*32+"!1 __EOA(i or ii)"

import re
from time import perf_counter

regex = """^([a-z]+?\.[a-z]+)+\%$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "aaa." * i * 1 + "!1 __EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")