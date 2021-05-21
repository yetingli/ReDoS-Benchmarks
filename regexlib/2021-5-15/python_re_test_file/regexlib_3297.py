# 3297
# &lt;a[a-zA-Z0-9 =&quot;'.?_/]*(href\s*=\s*){1}[a-zA-Z0-9 =&quot;'.?_/]*\s*((/&gt;)|(&gt;[a-zA-Z0-9 =&quot;'&lt;&gt;.?_/]*&lt;/a&gt;))
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"/&gt;&lt;ahref="+"&gt;"*5000+"!1 _SLQ_2"

import re
from time import perf_counter

regex = """&lt;a[a-zA-Z0-9 =&quot;'.?_/]*(href\s*=\s*){1}[a-zA-Z0-9 =&quot;'.?_/]*\s*((/&gt;)|(&gt;[a-zA-Z0-9 =&quot;'&lt;&gt;.?_/]*&lt;/a&gt;))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "/&gt;&lt;ahref=" + "&gt;" * i * 10000 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")