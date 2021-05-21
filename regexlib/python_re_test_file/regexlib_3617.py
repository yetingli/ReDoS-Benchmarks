# 3617
# ^START(?=(?:.(?!END|START))*MIDDLE).*?END[^\n]+
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"START=MIDDLEEND"*5000+"@1 _SLQ_2\n"

import re
from time import perf_counter

regex = """^START(?=(?:.(?!END|START))*MIDDLE).*?END[^\n]+"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "START=MIDDLEEND" * i * 10000 + "@1 _SLQ_2\n"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")