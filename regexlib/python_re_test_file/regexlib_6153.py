# 6153
# ([^_.]([a-zA-Z0-9_]*[.]?[a-zA-Z0-9_]+[^_]){2})@([a-z0-9]+[.]([a-z]{2,3}|[a-z]{2,3}[.][a-z]{2,3}))
# EXPONENT
# nums:4
# EXPONENT AttackString:"@a@a@"+"0000"*32+"◎1 __EOA(iii)"

import re
from time import perf_counter

regex = """([^_.]([a-zA-Z0-9_]*[.]?[a-zA-Z0-9_]+[^_]){2})@([a-z0-9]+[.]([a-z]{2,3}|[a-z]{2,3}[.][a-z]{2,3}))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "@a@a@" + "0000" * i * 1 + "◎1 __EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")