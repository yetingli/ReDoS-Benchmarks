# 1167
# ^(([a-zA-Z0-9]+([\-])?[a-zA-Z0-9]+)+(\.)?)+[a-zA-Z]{2,6}$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"000"*8+"!1 __EOA(i or ii)"

import re2 as re
from time import perf_counter

regex = """^(([a-zA-Z0-9]+([\-])?[a-zA-Z0-9]+)+(\.)?)+[a-zA-Z]{2,6}$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "000" * i * 1 + "!1 __EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")