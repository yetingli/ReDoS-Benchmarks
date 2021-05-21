# 5965
# <\s*/?\s*\w+(\s*\w+\s*=\s*(['"][^'"]*['"]|[\w#]+))*\s*/?\s*>
# EXPONENT
# nums:4
# EXPONENT AttackString:"<1"+"000="*32+"! _1_EOA(i or ii)"

import re
from time import perf_counter

regex = """<\s*/?\s*\w+(\s*\w+\s*=\s*(['"][^'"]*['"]|[\w#]+))*\s*/?\s*>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<1" + "000=" * i * 1 + "! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")