# 1485
# &lt;a [a-zA-Z0-9 =&quot;'.:;?]*href=*[a-zA-Z0-9 =&quot;'.:;&gt;?]*[^&gt;]*&gt;([a-zA-Z0-9 =&quot;'.:;&gt;?]*[^&lt;]*&lt;)\s*/a\s*&gt;
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"&lt;a href"*256+"@1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """&lt;a [a-zA-Z0-9 =&quot;'.:;?]*href=*[a-zA-Z0-9 =&quot;'.:;&gt;?]*[^&gt;]*&gt;([a-zA-Z0-9 =&quot;'.:;&gt;?]*[^&lt;]*&lt;)\s*/a\s*&gt;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "&lt;a href" * i * 1 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")