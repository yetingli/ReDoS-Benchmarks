# 3744
# ^Content-Type:\s*(\w+)\s*/?\s*(\w*)?\s*;\s*((\w+)?\s*=\s*((".+")|(\S+)))?
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"Content-Type:1"+"\t"*5000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """^Content-Type:\s*(\w+)\s*/?\s*(\w*)?\s*;\s*((\w+)?\s*=\s*((".+")|(\S+)))?"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "Content-Type:1" + "\t" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")