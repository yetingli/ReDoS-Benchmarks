# 1735
# ^(\w+([_.]{1}\w+)*@\w+([_.]{1}\w+)*\.[A-Za-z]{2,3}[;]?)*$
# EXPONENT
# nums:5
# EXPONENT AttackString:"1@1"+"_"*32+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """^(\w+([_.]{1}\w+)*@\w+([_.]{1}\w+)*\.[A-Za-z]{2,3}[;]?)*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1@1" + "_" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")