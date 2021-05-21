# 7002
# .*[Pp]re[Ss\$]cr[iI1]pt.*
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"1"*20000+"!1 _SLQ_1"

import re2 as re
from time import perf_counter

regex = """.*[Pp]re[Ss\$]cr[iI1]pt.*"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1" * i * 10000 + "!1 _SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")