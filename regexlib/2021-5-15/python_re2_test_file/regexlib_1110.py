# 1110
# ([+(]?\d{0,2}[)]?)([-/.\s]?\d+)+
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"0"*32+"!1 __NQ"

import re2 as re
from time import perf_counter

regex = """([+(]?\d{0,2}[)]?)([-/.\s]?\d+)+"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0" * i * 1 + "!1 __NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")