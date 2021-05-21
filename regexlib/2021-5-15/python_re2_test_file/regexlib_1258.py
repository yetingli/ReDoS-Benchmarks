# 1258
# .*?((?:\b|\+)\d[\d \-\(\)]+\d)\b.*
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"0 "*5000+"! _1_POA(i)\n"

import re2 as re
from time import perf_counter

regex = """.*?((?:\b|\+)\d[\d \-\(\)]+\d)\b.*"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0 " * i * 10000 + "! _1_POA(i)\n"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")