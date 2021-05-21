# 2744
# ([0-9a-z_-]+[\.][0-9a-z_-]{1,3})$
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"0"*10000+"!1 _!1 _SLQ_1"

import re2 as re
from time import perf_counter

regex = """([0-9a-z_-]+[\.][0-9a-z_-]{1,3})$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0" * i * 10000 + "!1 _!1 _SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")