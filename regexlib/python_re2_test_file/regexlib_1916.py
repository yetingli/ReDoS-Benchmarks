# 1916
# ^(([1-9]{1}(\d+)?)(\.\d+)?)|([0]\.(\d+)?([1-9]{1})(\d+)?)$
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"0."+"1"*10000+"!1 __POA(i)"

import re2 as re
from time import perf_counter

regex = """^(([1-9]{1}(\d+)?)(\.\d+)?)|([0]\.(\d+)?([1-9]{1})(\d+)?)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "0." + "1" * i * 10000 + "!1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")