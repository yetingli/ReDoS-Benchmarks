# 3693
# \b(\w+).\1
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"11"*80000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """\b(\w+).\1"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "11" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")