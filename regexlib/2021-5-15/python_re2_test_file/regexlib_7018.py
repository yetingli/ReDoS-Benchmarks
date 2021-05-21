# 7018
# ^([a-zA-Z](?:(?:(?:\w[\.\_]?)*)\w)+)([a-zA-Z0-9])$
# EXPONENT
# nums:5
# EXPONENT AttackString:"a"+"_"*32+"!1 __EOA(iii)"

import re2 as re
from time import perf_counter

regex = """^([a-zA-Z](?:(?:(?:\w[\.\_]?)*)\w)+)([a-zA-Z0-9])$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "a" + "_" * i * 1 + "!1 __EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")