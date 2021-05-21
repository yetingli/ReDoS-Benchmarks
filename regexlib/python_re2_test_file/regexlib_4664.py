# 4664
# ^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$
# EXPONENT
# nums:5
# EXPONENT AttackString:"1"+"1"*32+"! _1_NQ"

import re2 as re
from time import perf_counter

regex = """^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1" + "1" * i * 1 + "! _1_NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")