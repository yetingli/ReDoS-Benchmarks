# 4861
# ^[0-9]{6}-(?:[0-9]+){1,3}[0-9A-Za-z]$
# EXPONENT
# nums:4
# EXPONENT AttackString:"000000-"+"0"*512+"!1 __NQ"

import re
from time import perf_counter

regex = """^[0-9]{6}-(?:[0-9]+){1,3}[0-9A-Za-z]$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "000000-" + "0" * i * 1 + "!1 __NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")