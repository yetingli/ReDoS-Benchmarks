# 6845
# &lt;img .+ src[ ]*=[ ]*\&quot;(.+)\&quot;
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"&lt;img 1 src="*5000+"!1 _SLQ_2"

import re
from time import perf_counter

regex = """&lt;img .+ src[ ]*=[ ]*\&quot;(.+)\&quot;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "&lt;img 1 src=" * i * 10000 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")