# 3232
# [a-z0-9][a-z0-9_\.-]{0,}[a-z0-9]\.[a-z0-9][a-z0-9_\.-]{0,}[a-z0-9][\.][cn]{2,4}
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"a"+"0.0"*5000+"!1 __POA(i)"

import re2 as re
from time import perf_counter

regex = """[a-z0-9][a-z0-9_\.-]{0,}[a-z0-9]\.[a-z0-9][a-z0-9_\.-]{0,}[a-z0-9][\.][cn]{2,4}"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "a" + "0.0" * i * 10000 + "!1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")