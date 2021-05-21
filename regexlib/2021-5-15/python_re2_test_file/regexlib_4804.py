# 4804
# ^(\+[0-9]{2,}[0-9]{4,}[0-9]*)(x?[0-9]{1,})?$
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"+00"+"0000"*5000+"◎@! _1_POA(i)"

import re2 as re
from time import perf_counter

regex = """^(\+[0-9]{2,}[0-9]{4,}[0-9]*)(x?[0-9]{1,})?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "+00" + "0000" * i * 10000 + "◎@! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")