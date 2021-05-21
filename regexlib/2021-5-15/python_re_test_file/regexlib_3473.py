# 3473
# ^(\d|,)*\.?\d*$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"2"*10000+"◎@! _1! _1! _1!\n_SLQ_3"

import re
from time import perf_counter

regex = """^(\d|,)*\.?\d*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "2" * i * 10000 + "◎@! _1! _1! _1!\n_SLQ_3"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")