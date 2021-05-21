# 1114
# ^p(ost)?[ |\.]*o(ffice)?[ |\.]*(box)?[ 0-9]*[^[a-z ]]*
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"po"+" "*5000+"! _1_POA(i)"

import re2 as re
from time import perf_counter

regex = """^p(ost)?[ |\.]*o(ffice)?[ |\.]*(box)?[ 0-9]*[^[a-z ]]*"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "po" + " " * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")