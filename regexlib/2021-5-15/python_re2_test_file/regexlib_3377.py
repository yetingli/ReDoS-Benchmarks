# 3377
# (.*)-----(BEGIN|END)([^-]*)-----(.*)
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"-----BEGIN-----"*5000+"! _1SLQ_2\n"

import re2 as re
from time import perf_counter

regex = """(.*)-----(BEGIN|END)([^-]*)-----(.*)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "-----BEGIN-----" * i * 10000 + "! _1SLQ_2\n"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")