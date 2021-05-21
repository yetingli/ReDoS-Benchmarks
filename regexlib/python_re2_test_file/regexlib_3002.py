# 3002
# [A-Za-z_.0-9-]+@{1}[a-z]+([.]{1}[a-z]{2,4})+
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"A"*10000+"! _1SLQ_1"

import re2 as re
from time import perf_counter

regex = """[A-Za-z_.0-9-]+@{1}[a-z]+([.]{1}[a-z]{2,4})+"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "A" * i * 10000 + "! _1SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")