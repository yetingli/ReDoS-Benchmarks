# 2817
# (?s)/\*.*\*/
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"s/*"*10000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """(?s)/\*.*\*/"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "s/*" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")