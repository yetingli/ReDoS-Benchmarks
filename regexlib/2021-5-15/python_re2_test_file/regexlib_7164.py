# 7164
# [-\w$%&'*+\/=?^_`{|}~.]+@(?<domain>[-a-zA-Z0-9_]+\.*[-a-zA-Z0-9]+\.\.*[-a-zA-Z0-9]+\.[a-zA-Z0-9]{2,7})$
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"-@"+"-"*5000+"◎@! _1SLQ_2"

import re2 as re
from time import perf_counter

regex = """[-\w$%&'*+\/=?^_`{|}~.]+@(?<domain>[-a-zA-Z0-9_]+\.*[-a-zA-Z0-9]+\.\.*[-a-zA-Z0-9]+\.[a-zA-Z0-9]{2,7})$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "-@" + "-" * i * 10000 + "◎@! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")