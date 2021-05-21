# 4902
# ^(([a-z])+.)+[A-Z]([a-z])+$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"a"*64+"!1 __EOA(iv)"

import re2 as re
from time import perf_counter

regex = """^(([a-z])+.)+[A-Z]([a-z])+$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "a" * i * 1 + "!1 __EOA(iv)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")