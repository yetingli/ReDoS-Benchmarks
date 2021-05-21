# 3420
# \w+\S?\w+\s?(@|\W(at)\W)\s?\w+\s?(\.|\W(dot)\W)\s?\w+\.?\w+
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"1"*512+"! _1SLQ_2"

import re
from time import perf_counter

regex = """\w+\S?\w+\s?(@|\W(at)\W)\s?\w+\s?(\.|\W(dot)\W)\s?\w+\.?\w+"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")