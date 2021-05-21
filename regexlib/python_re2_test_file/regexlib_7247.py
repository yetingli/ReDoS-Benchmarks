# 7247
# ^([0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*@([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z]{2,9})$
# EXPONENT
# nums:5
# EXPONENT AttackString:"0"+"0"*32+"!1 __EOA(iii)"

import re2 as re
from time import perf_counter

regex = """^([0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*@([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z]{2,9})$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "0" + "0" * i * 1 + "!1 __EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")