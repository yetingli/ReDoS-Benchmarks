# 3254
# ^(\S+\.{1})(\S+\.{1})*([^\s\.]+\s*)$
# EXPONENT
# nums:5
# EXPONENT AttackString:".."+"."*32+"@1 __EOA(iv)"

import re2 as re
from time import perf_counter

regex = """^(\S+\.{1})(\S+\.{1})*([^\s\.]+\s*)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = ".." + "." * i * 1 + "@1 __EOA(iv)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")