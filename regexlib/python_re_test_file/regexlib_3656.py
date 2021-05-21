# 3656
# <a[\s](?!.*\b(title)\b)[^>]+>
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"<a !title"*5000+"@1 _SLQ_2"

import re
from time import perf_counter

regex = """<a[\s](?!.*\b(title)\b)[^>]+>"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "<a !title" * i * 10000 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")