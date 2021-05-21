# 6733
# ^0*(\d{1,3}(\.?\d{3})*)\-?([\dkK])$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"0"*5000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """^0*(\d{1,3}(\.?\d{3})*)\-?([\dkK])$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")