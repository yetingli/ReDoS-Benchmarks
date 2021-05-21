# 6155
# (?:\d|I{1,3})?\s?\w{2,}\.?\s*\d{1,}\:\d{1,}-?,?\d{0,2}(?:,\d{0,2}){0,2}
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"11"*512+"!_1SLQ_2"

import re
from time import perf_counter

regex = """(?:\d|I{1,3})?\s?\w{2,}\.?\s*\d{1,}\:\d{1,}-?,?\d{0,2}(?:,\d{0,2}){0,2}"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "11" * i * 1 + "!_1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")