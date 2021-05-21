# 5473
# ^\s*([A-Z\s])([a-z\s]){1,30}([A-Z\s])([a-z\s]){1,30}\s*$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"A"+"\t\t"*20000+"!_1_POA(i)"

import re
from time import perf_counter

regex = """^\s*([A-Z\s])([a-z\s]){1,30}([A-Z\s])([a-z\s]){1,30}\s*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "A" + "\t\t" * i * 10000 + "!_1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")