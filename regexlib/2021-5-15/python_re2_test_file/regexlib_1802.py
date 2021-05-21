# 1802
# (\[(\w+)\s*(([\w]*)=('|&quot;)?([a-zA-Z0-9|:|\/|=|-|.|\?|&amp;]*)(\5)?)*\])([a-zA-Z0-9|:|\/|=|-|.|\?|&amp;|\s]+)(\[\/\2\])
# EXPONENT
# nums:5
# EXPONENT AttackString:"[1"+"=&quot;"*16+"◎@! _1_EOA(i or ii)"

import re2 as re
from time import perf_counter

regex = """(\[(\w+)\s*(([\w]*)=('|&quot;)?([a-zA-Z0-9|:|\/|=|-|.|\?|&amp;]*)(\5)?)*\])([a-zA-Z0-9|:|\/|=|-|.|\?|&amp;|\s]+)(\[\/\2\])"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "[1" + "=&quot;" * i * 1 + "◎@! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")