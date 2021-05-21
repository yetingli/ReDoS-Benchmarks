# 777
# ([A-Z][\w\d\.\-]+)(?:(?:\+)([\w\d\.\-]+))?@([A-Z0-9][\w\.-]*[A-Z0-9]\.[A-Z][A-Z\.]*[A-Z])
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"A1@"+"AA.A"*5000+"!1 _SLQ_2"

import re
from time import perf_counter

regex = """([A-Z][\w\d\.\-]+)(?:(?:\+)([\w\d\.\-]+))?@([A-Z0-9][\w\.-]*[A-Z0-9]\.[A-Z][A-Z\.]*[A-Z])"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "A1@" + "AA.A" * i * 10000 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")