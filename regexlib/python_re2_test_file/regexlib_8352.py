# 8352
# ^([a-zA-Z0-9])(([\-.]|[_]+)?([a-zA-Z0-9]+))*(@){1}([a-z0-9]|([a-z0-9][\-]))+[.]{1}(([a-z]{2,3})|([a-z]{2,3}[.]{1}[a-z]{2,3}))$
# EXPONENT
# nums:5
# EXPONENT AttackString:"a"+"a"*32+"!1 __NQ"

import re2 as re
from time import perf_counter

regex = """^([a-zA-Z0-9])(([\-.]|[_]+)?([a-zA-Z0-9]+))*(@){1}([a-z0-9]|([a-z0-9][\-]))+[.]{1}(([a-z]{2,3})|([a-z]{2,3}[.]{1}[a-z]{2,3}))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "a" + "a" * i * 1 + "!1 __NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")