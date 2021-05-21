# 8548
# (?:\b\w*(\w\w?)\1{2,}\w*\b)
# EXPONENT
# nums:5
# EXPONENT AttackString:"111"+"00"*512+"! _1_EOA(iii)"

import re2 as re
from time import perf_counter

regex = """(?:\b\w*(\w\w?)\1{2,}\w*\b)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "111" + "00" * i * 1 + "! _1_EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")