# 3601
# \|(http.*)\|(.*)$/ig
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"|http|"*512+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """\|(http.*)\|(.*)$/ig"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "|http|" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")