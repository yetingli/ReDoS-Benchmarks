# 8359
# ^\d+?[A-Za-z]*\s\w*\s?\w+?\s\w{2}\w*\s*\w*$
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"1 1 11"+"00"*5000+"! _1_POA(i)"

import re2 as re
from time import perf_counter

regex = """^\d+?[A-Za-z]*\s\w*\s?\w+?\s\w{2}\w*\s*\w*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1 1 11" + "00" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")