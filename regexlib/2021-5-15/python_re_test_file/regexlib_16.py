# 16
# ^\d*[0-9](|.\d*[0-9]|)*$
# EXPONENT
# nums:4
# EXPONENT AttackString:"0"+"1"*32+"! _1SLQ_2"

import re
from time import perf_counter

regex = """^\d*[0-9](|.\d*[0-9]|)*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "0" + "1" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")