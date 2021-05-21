# 3304
# (\w+[\.\_\-]*)*\w+@[\w]+(.)*\w+$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"1"*32+"!1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """(\w+[\.\_\-]*)*\w+@[\w]+(.)*\w+$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1" * i * 1 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")