# 851
# [\w-]+@([\w-]+\.)+[\w-]+
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"1"*20000+"! _1SLQ_1"

import re
from time import perf_counter

regex = """[\w-]+@([\w-]+\.)+[\w-]+"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1" * i * 10000 + "! _1SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")