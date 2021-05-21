# 1466
# ^((?:(?:(?:\w[\.\-\+]?)*)\w)+)\@((?:(?:(?:\w[\.\-\+]?){0,62})\w)+)\.(\w{2,6})$
# EXPONENT
# nums:4
# EXPONENT AttackString:"1@"+"0"*32+"! _1_EOA(iii)"

import re
from time import perf_counter

regex = """^((?:(?:(?:\w[\.\-\+]?)*)\w)+)\@((?:(?:(?:\w[\.\-\+]?){0,62})\w)+)\.(\w{2,6})$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1@" + "0" * i * 1 + "! _1_EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")