# 294
# ^\s*([\(]?)\[?\s*\d{3}\s*\]?[\)]?\s*[\-]?[\.]?\s*\d{3}\s*[\-]?[\.]?\s*\d{4}$
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"111111"+"\t"*10000+"!_1_POA(i)"

import re2 as re
from time import perf_counter

regex = """^\s*([\(]?)\[?\s*\d{3}\s*\]?[\)]?\s*[\-]?[\.]?\s*\d{3}\s*[\-]?[\.]?\s*\d{4}$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "111111" + "\t" * i * 10000 + "!_1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")