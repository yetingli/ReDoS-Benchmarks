# 1087
# ^[^']*?\&lt;\s*Assembly\s*:\s*AssemblyVersion\s*\(\s*&quot;(\*|[0-9]+.\*|[0-9]+.[0-9]+.\*|[0-9]+.[0-9]+.[0-9]+.\*|[0-9]+.[0-9]+.[0-9]+.[0-9]+)&quot;\s*\)\s*\&gt;.*$
# EXPONENT
# nums:5
# EXPONENT AttackString:"*01*0101*010101*&lt;Assembly:AssemblyVersion(&quot;"+"0101"*64+"!1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """^[^']*?\&lt;\s*Assembly\s*:\s*AssemblyVersion\s*\(\s*&quot;(\*|[0-9]+.\*|[0-9]+.[0-9]+.\*|[0-9]+.[0-9]+.[0-9]+.\*|[0-9]+.[0-9]+.[0-9]+.[0-9]+)&quot;\s*\)\s*\&gt;.*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "*01*0101*010101*&lt;Assembly:AssemblyVersion(&quot;" + "0101" * i * 1 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")