# 3347
# ^[+-]? *(\$)? *((\d+)|(\d{1,3})(\,\d{3})*)(\.\d{0,2})?$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+" "*5000+"!1 __POA(i)"

import re
from time import perf_counter

regex = """^[+-]? *(\$)? *((\d+)|(\d{1,3})(\,\d{3})*)(\.\d{0,2})?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + " " * i * 10000 + "!1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")