# 6998
# .*[\$Ss]pecia[l1]\W[Oo0]ffer.*
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"$pecial$Offer"*5000+"! _1SLQ_2\n"

import re
from time import perf_counter

regex = """.*[\$Ss]pecia[l1]\W[Oo0]ffer.*"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "$pecial$Offer" * i * 10000 + "! _1SLQ_2\n"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")