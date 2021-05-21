# 8414
# (NOT)?(\s*\(*)\s*(\w+)\s*(=|&lt;&gt;|&lt;|&gt;|LIKE|IN)\s*(\(([^\)]*)\)|'([^']*)'|(-?\d*\.?\d+))(\s*\)*\s*)(AND|OR)?
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"1="+"("*10000+"@1 _SLQ_2"

import re
from time import perf_counter

regex = """(NOT)?(\s*\(*)\s*(\w+)\s*(=|&lt;&gt;|&lt;|&gt;|LIKE|IN)\s*(\(([^\)]*)\)|'([^']*)'|(-?\d*\.?\d+))(\s*\)*\s*)(AND|OR)?"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1=" + "(" * i * 10000 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")