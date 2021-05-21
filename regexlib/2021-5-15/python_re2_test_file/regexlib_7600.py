# 7600
# ^[a-z]+([a-z0-9-]*[a-z0-9]+)?(\.([a-z]+([a-z0-9-]*[a-z0-9]+)?)+)*$
# EXPONENT
# nums:5
# EXPONENT AttackString:"a."+"aa"*8+"!1 __EOA(i or ii)"

import re2 as re
from time import perf_counter

regex = """^[a-z]+([a-z0-9-]*[a-z0-9]+)?(\.([a-z]+([a-z0-9-]*[a-z0-9]+)?)+)*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "a." + "aa" * i * 1 + "!1 __EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")