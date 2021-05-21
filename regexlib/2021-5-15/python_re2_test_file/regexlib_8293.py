# 8293
# ((&quot;|')[a-z0-9\/\.\?\=\&amp;]*(\.htm|\.asp|\.php|\.jsp)[a-z0-9\/\.\?\=\&amp;]*(&quot;|'))|(href=*?[a-z0-9\/\.\?\=\&amp;&quot;']*)
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"&quot;"*5000+"!1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """((&quot;|')[a-z0-9\/\.\?\=\&amp;]*(\.htm|\.asp|\.php|\.jsp)[a-z0-9\/\.\?\=\&amp;]*(&quot;|'))|(href=*?[a-z0-9\/\.\?\=\&amp;&quot;']*)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "&quot;" * i * 10000 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")