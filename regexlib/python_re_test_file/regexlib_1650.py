# 1650
# ^(?:(?:((?![0-9_])[a-zA-Z0-9_]+)\.?)+)(?<!\.)$
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"a"*32+"!1 __NQ"

import re
from time import perf_counter

regex = """^(?:(?:((?![0-9_])[a-zA-Z0-9_]+)\.?)+)(?<!\.)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "a" * i * 1 + "!1 __NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")