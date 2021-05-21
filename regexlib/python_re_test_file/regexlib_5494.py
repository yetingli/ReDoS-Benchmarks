# 5494
# ^.*(?=.{6,10})(?=.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z])(?=.*\d.*\d).*$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"==111111=aaaa"+"1"*10000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """^.*(?=.{6,10})(?=.*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z])(?=.*\d.*\d).*$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "==111111=aaaa" + "1" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")