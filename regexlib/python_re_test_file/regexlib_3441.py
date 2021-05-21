# 3441
# [a-zA-Z]{1}[a-zA-Z0-9\-._]+@([a-zA-Z0-9-]+\.)+\w+
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"a"*10000+"!1 _SLQ_2"

import re
from time import perf_counter

regex = """[a-zA-Z]{1}[a-zA-Z0-9\-._]+@([a-zA-Z0-9-]+\.)+\w+"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "a" * i * 10000 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")