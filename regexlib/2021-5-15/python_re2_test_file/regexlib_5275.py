# 5275
# ^([1-9]{1}(([0-9])?){2})+(,[0-9]{1}[0-9]{2})*$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"1"*32+"!1 __EOA(iii)"

import re2 as re
from time import perf_counter

regex = """^([1-9]{1}(([0-9])?){2})+(,[0-9]{1}[0-9]{2})*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1" * i * 1 + "!1 __EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")