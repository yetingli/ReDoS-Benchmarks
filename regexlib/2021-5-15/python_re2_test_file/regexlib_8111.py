# 8111
# (([A-Za-z0-9_\\-]+\\.?)*)[A-Za-z0-9_\\-]+\\.[A-Za-z0-9_\\-]{2,6}
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"-\\"*32+"!1 __EOA(iii)"

import re2 as re
from time import perf_counter

regex = """(([A-Za-z0-9_\\-]+\\.?)*)[A-Za-z0-9_\\-]+\\.[A-Za-z0-9_\\-]{2,6}"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "-\\" * i * 1 + "!1 __EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")