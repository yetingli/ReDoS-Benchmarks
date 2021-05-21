# 7144
# ((0)+(\.[1-9](\d)?))|((0)+(\.(\d)[1-9]+))|(([1-9]+(0)?)+(\.\d+)?)|(([1-9]+(0)?)+(\.\d+)?)
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"1"*32+"! _1_NQ"

import re
from time import perf_counter

regex = """((0)+(\.[1-9](\d)?))|((0)+(\.(\d)[1-9]+))|(([1-9]+(0)?)+(\.\d+)?)|(([1-9]+(0)?)+(\.\d+)?)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1" * i * 1 + "! _1_NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")