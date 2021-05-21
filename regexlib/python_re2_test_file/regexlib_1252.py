# 1252
# ((xmlns:.*?=[&quot;,'].*?[&quot;,'])|(xmlns=[&quot;,'].*?[&quot;,']))
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"xmlns:=&&"+"xmlns=&"*5000+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """((xmlns:.*?=[&quot;,'].*?[&quot;,'])|(xmlns=[&quot;,'].*?[&quot;,']))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "xmlns:=&&" + "xmlns=&" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")