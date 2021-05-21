# 1171
# ([A-Za-z0-9.]+\s*)+,
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"."*32+"!1 __NQ"

import re
from time import perf_counter

regex = """([A-Za-z0-9.]+\s*)+,"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "." * i * 1 + "!1 __NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")