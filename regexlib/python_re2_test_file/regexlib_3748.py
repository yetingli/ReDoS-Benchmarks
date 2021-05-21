# 3748
# ^(?:[\w]+[\&amp;\-_\.]*)+@(?:(?:[\w]+[\-_\.]*)\.(?:[a-zA-Z]{2,}?))$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"__"*16+"!1 __EOA(i or ii)"

import re2 as re
from time import perf_counter

regex = """^(?:[\w]+[\&amp;\-_\.]*)+@(?:(?:[\w]+[\-_\.]*)\.(?:[a-zA-Z]{2,}?))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "__" * i * 1 + "!1 __EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")