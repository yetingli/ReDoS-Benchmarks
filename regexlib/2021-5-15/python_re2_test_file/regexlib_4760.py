# 4760
# (<meta\s+)*((name\s*=\s*("|')(?<name>[^'("|')]*)("|')){1}|content\s*=\s*("|')(?<content>[^'("|')]*)("|')|scheme\s*=\s*("|')(?<scheme>[^'("|')]*)("|'))
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"<meta "*5000+"! _1SLQ_1"

import re2 as re
from time import perf_counter

regex = """(<meta\s+)*((name\s*=\s*("|')(?<name>[^'("|')]*)("|')){1}|content\s*=\s*("|')(?<content>[^'("|')]*)("|')|scheme\s*=\s*("|')(?<scheme>[^'("|')]*)("|'))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "<meta " * i * 10000 + "! _1SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")