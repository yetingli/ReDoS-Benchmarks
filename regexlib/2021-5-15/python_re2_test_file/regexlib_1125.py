# 1125
# (href=|url|import).*[\'"]([^(http:)].*css)[\'"]
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"href="*5000+"! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """(href=|url|import).*[\'"]([^(http:)].*css)[\'"]"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "href=" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")