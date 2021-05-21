# 1675
# (REM [\d\D]*?[\r\n])|(?<SL>\'[\d\D]*?[\r\n])
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"REM "*5000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """(REM [\d\D]*?[\r\n])|(?<SL>\'[\d\D]*?[\r\n])"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "REM " * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")