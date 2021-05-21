# 5265
# ^<\s*(td|TD)\s*(\w|\W)*\s*>(\w|\W)*</(td|TD)>$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"<td>"+"\t"*10000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """^<\s*(td|TD)\s*(\w|\W)*\s*>(\w|\W)*</(td|TD)>$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<td>" + "\t" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")