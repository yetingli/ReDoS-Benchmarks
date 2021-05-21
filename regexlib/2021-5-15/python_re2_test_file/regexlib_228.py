# 228
# ^([A-Za-z]|[A-Za-z][0-9]*|[0-9]*[A-Za-z])+$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"AA"*8+"!1 __EOD(ii2)"

import re2 as re
from time import perf_counter

regex = """^([A-Za-z]|[A-Za-z][0-9]*|[0-9]*[A-Za-z])+$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "AA" * i * 1 + "!1 __EOD(ii2)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")