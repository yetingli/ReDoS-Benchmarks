# 2424
# (UPDATE\s+)(\w+)\s+(SET)\s+([\w+\s*=\s*\w+,?\s*]+)\s+(WHERE.+)
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"UPDATE 1 SET 1"*5000+"!_1SLQ_2"

import re
from time import perf_counter

regex = """(UPDATE\s+)(\w+)\s+(SET)\s+([\w+\s*=\s*\w+,?\s*]+)\s+(WHERE.+)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "UPDATE 1 SET 1" * i * 10000 + "!_1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")