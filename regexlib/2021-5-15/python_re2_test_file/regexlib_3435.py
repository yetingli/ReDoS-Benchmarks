# 3435
# (ISBN[-]*(1[03])*[ ]*(: ){0,1})*(([0-9Xx][- ]*){13}|([0-9Xx][- ]*){10})
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"ISBN-10 : "*5000+"!1 _SLQ_1"

import re2 as re
from time import perf_counter

regex = """(ISBN[-]*(1[03])*[ ]*(: ){0,1})*(([0-9Xx][- ]*){13}|([0-9Xx][- ]*){10})"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "ISBN-10 : " * i * 10000 + "!1 _SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")