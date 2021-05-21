# 1641
# <a\s+(?:(?:\w+\s*=\s*)(?:\w+|"[^"]*"|'[^']*'))*?\s*href\s*=\s*(?<url>\w+|"[^"]*"|'[^']*')(?:(?:\s+\w+\s*=\s*)(?:\w+|"[^"]*"|'[^']*'))*?>.+?</a>
# EXPONENT
# nums:5
# EXPONENT AttackString:"<a "+"000="*32+"! _1_EOA(i or ii)"

import re2 as re
from time import perf_counter

regex = """<a\s+(?:(?:\w+\s*=\s*)(?:\w+|"[^"]*"|'[^']*'))*?\s*href\s*=\s*(?<url>\w+|"[^"]*"|'[^']*')(?:(?:\s+\w+\s*=\s*)(?:\w+|"[^"]*"|'[^']*'))*?>.+?</a>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<a " + "000=" * i * 1 + "! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")