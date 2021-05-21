# 3296
# &lt;a[a-zA-Z0-9 =&quot;'.:;?]*(name=){1}[a-zA-Z0-9 =&quot;'.:;?]*\s*((/&gt;)|(&gt;[a-zA-Z0-9 =&quot;'&lt;&gt;.:;?]*&lt;/a&gt;))
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"&lt;aname="*256+"!_1SLQ_2"

import re
from time import perf_counter

regex = """&lt;a[a-zA-Z0-9 =&quot;'.:;?]*(name=){1}[a-zA-Z0-9 =&quot;'.:;?]*\s*((/&gt;)|(&gt;[a-zA-Z0-9 =&quot;'&lt;&gt;.:;?]*&lt;/a&gt;))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "&lt;aname=" * i * 1 + "!_1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")