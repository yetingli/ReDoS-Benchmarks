# 8344
# (?s)<tr[^>]*>(?<content>.*?)</tr>
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"s<tr>"*5000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """(?s)<tr[^>]*>(?<content>.*?)</tr>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "s<tr>" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")