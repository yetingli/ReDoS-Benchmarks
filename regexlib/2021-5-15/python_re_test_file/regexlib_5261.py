# 5261
# ((\d{1,5})*\.*(\d{0,3})"[W|D|H|DIA][X|\s]).*
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"0"*32+"! _1_NQ"

import re
from time import perf_counter

regex = """((\d{1,5})*\.*(\d{0,3})"[W|D|H|DIA][X|\s]).*"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0" * i * 1 + "! _1_NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")