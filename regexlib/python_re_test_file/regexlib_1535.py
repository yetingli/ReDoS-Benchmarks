# 1535
# ^([0-9a-zA-Z]+[-._+&amp;])*[0-9a-zA-Z_-]+@([-0-9a-zA-Z]+[.])+[a-zA-Z]{2,6}$
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"a"*32+"!1 __EOA(iv)"

import re
from time import perf_counter

regex = """^([0-9a-zA-Z]+[-._+&amp;])*[0-9a-zA-Z_-]+@([-0-9a-zA-Z]+[.])+[a-zA-Z]{2,6}$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "a" * i * 1 + "!1 __EOA(iv)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")