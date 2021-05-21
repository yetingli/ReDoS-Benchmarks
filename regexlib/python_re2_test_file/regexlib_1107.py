# 1107
# ^[-+]?(?:\d+\.?|\.\d)\d*(?:[Ee][-+]?\d+)?$
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"1"*10000+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """^[-+]?(?:\d+\.?|\.\d)\d*(?:[Ee][-+]?\d+)?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")