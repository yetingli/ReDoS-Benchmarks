# 2400
# ^[+]?((\d*[1-9]+\d*\.?\d*)|(\d*\.\d*[1-9]+\d*))$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"1"*256+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """^[+]?((\d*[1-9]+\d*\.?\d*)|(\d*\.\d*[1-9]+\d*))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")