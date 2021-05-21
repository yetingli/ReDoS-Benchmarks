# 8651
# (^\d*\.?\d*[0-9]+\d*$)|(^[0-9]+\d*\.\d*$)
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"0"*256+"! _1SLQ_2"

import re
from time import perf_counter

regex = """(^\d*\.?\d*[0-9]+\d*$)|(^[0-9]+\d*\.\d*$)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")