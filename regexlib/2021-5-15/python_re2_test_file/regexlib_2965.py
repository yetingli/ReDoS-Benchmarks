# 2965
# &lt;(\/{0,1})img(.*?)(\/{0,1})\&gt;
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"&lt;img"*5000+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """&lt;(\/{0,1})img(.*?)(\/{0,1})\&gt;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "&lt;img" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")