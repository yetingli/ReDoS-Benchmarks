# 1626
# ([A-Z]:\\[^/:\*\?<>\|]+\.\w{2,6})|(\\{2}[^/:\*\?<>\|]+\.\w{2,6})
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"\\\\"*5000+"@1 _SLQ_1"

import re
from time import perf_counter

regex = """([A-Z]:\\[^/:\*\?<>\|]+\.\w{2,6})|(\\{2}[^/:\*\?<>\|]+\.\w{2,6})"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "\\\\" * i * 10000 + "@1 _SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")