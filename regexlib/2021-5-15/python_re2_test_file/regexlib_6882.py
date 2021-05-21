# 6882
# ^\+?[a-z0-9](([-+.]|[_]+)?[a-z0-9]+)*@([a-z0-9]+(\.|\-))+[a-z]{2,6}$
# EXPONENT
# nums:5
# EXPONENT AttackString:"a"+"0"*32+"◎@! _1_NQ"

import re2 as re
from time import perf_counter

regex = """^\+?[a-z0-9](([-+.]|[_]+)?[a-z0-9]+)*@([a-z0-9]+(\.|\-))+[a-z]{2,6}$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "a" + "0" * i * 1 + "◎@! _1_NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")