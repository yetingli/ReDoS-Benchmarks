# 7246
# ^(\d)?[ ]*[\(\.\-]?(\d{3})[\)\.\-]?[ ]*(\d{3})[\.\- ]?(\d{4})[ ]*(x|ext\.?)?[ ]*(\d{1,7})?$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"1111111111"+" "*5000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """^(\d)?[ ]*[\(\.\-]?(\d{3})[\)\.\-]?[ ]*(\d{3})[\.\- ]?(\d{4})[ ]*(x|ext\.?)?[ ]*(\d{1,7})?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1111111111" + " " * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")