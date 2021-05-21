# 3488
# ^[a-zA-Z\d]+(([\'\,\.\- #][a-zA-Z\d ])?[a-zA-Z\d]*[\.]*)*$
# EXPONENT
# nums:4
# EXPONENT AttackString:"a"+"a"*32+"!1 __NQ"

import re
from time import perf_counter

regex = """^[a-zA-Z\d]+(([\'\,\.\- #][a-zA-Z\d ])?[a-zA-Z\d]*[\.]*)*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "a" + "a" * i * 1 + "!1 __NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")