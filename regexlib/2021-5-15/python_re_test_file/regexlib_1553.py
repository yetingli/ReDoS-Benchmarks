# 1553
# (([a-zA-Z0-9\-]*\.{1,}){1,}[a-zA-Z0-9]*)
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"."*32+"!1 __NQ"

import re
from time import perf_counter

regex = """(([a-zA-Z0-9\-]*\.{1,}){1,}[a-zA-Z0-9]*)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "." * i * 1 + "!1 __NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")