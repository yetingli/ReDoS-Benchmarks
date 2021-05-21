# 258
# (?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}\.?\t*\s*){2}\(\r*\n*([0-9]{1,})
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"a.aa"*128+"!_1SLQ_2"

import re
from time import perf_counter

regex = """(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}\.?\t*\s*){2}\(\r*\n*([0-9]{1,})"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "a.aa" * i * 1 + "!_1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")