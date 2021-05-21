# 3528
# ^([a-zA-Z]+[\'\,\.\-]?[a-zA-Z ]*)+[ ]([a-zA-Z]+[\'\,\.\-]?[a-zA-Z ]+)+$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"AA"*16+"!1 __EOA(i or ii)"

import re2 as re
from time import perf_counter

regex = """^([a-zA-Z]+[\'\,\.\-]?[a-zA-Z ]*)+[ ]([a-zA-Z]+[\'\,\.\-]?[a-zA-Z ]+)+$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "AA" * i * 1 + "!1 __EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")