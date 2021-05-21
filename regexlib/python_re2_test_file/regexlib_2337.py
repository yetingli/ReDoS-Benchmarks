# 2337
# ^<a[^>]*(http://[^"]*)[^>]*>([ 0-9a-zA-Z]+)</a>$
# EXPONENT
# nums:5
# EXPONENT AttackString:"<a"+"http://"*256+"@1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """^<a[^>]*(http://[^"]*)[^>]*>([ 0-9a-zA-Z]+)</a>$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<a" + "http://" * i * 1 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")