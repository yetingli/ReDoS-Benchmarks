# 2960
# [^\\]+(?=(\.dwg)|(\.pdf)|(\.doc[^x]))
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"="*10000+"! _1SLQ_1"

import re
from time import perf_counter

regex = """[^\\]+(?=(\.dwg)|(\.pdf)|(\.doc[^x]))"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "=" * i * 10000 + "! _1SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")