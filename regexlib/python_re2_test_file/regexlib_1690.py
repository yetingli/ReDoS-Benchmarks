# 1690
# ^((([a-z0-9])+([\w.-]{1})?)+([^\W_]{1}))+@((([a-z0-9])+([\w-]{1})?)+([^\W_]{1}))+\.[a-z]{2,3}(\.[a-z]{2,4})?$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"0"*16+"!1 __EOA(iii)"

import re2 as re
from time import perf_counter

regex = """^((([a-z0-9])+([\w.-]{1})?)+([^\W_]{1}))+@((([a-z0-9])+([\w-]{1})?)+([^\W_]{1}))+\.[a-z]{2,3}(\.[a-z]{2,4})?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0" * i * 1 + "!1 __EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")