# 4877
# ^(?:(?:[\w\.\-_]+@[\w\d]+(?:\.[\w]{2,6})+)[,;]?\s?)+$
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"0000@0."*32+"!1 __EOA(i or ii)"

import re
from time import perf_counter

regex = """^(?:(?:[\w\.\-_]+@[\w\d]+(?:\.[\w]{2,6})+)[,;]?\s?)+$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0000@0." * i * 1 + "!1 __EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")