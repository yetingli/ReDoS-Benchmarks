# 3324
# <(script|style)[^>]*?>(?:.|\n)*?</\s*\1\s*>
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"<script></script"*5000+"!_1SLQ_2"

import re
from time import perf_counter

regex = """<(script|style)[^>]*?>(?:.|\n)*?</\s*\1\s*>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "<script></script" * i * 10000 + "!_1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")