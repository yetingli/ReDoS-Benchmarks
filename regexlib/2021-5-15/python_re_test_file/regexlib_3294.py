# 3294
# ^\s*[a-zA-Z,\s]+\s*$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"\t"*5000+"!_1_POA(i)"

import re
from time import perf_counter

regex = """^\s*[a-zA-Z,\s]+\s*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "\t" * i * 10000 + "!_1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")