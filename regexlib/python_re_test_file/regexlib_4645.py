# 4645
# ^([1-9]+\d{0,2},(\d{3},)*\d{3}(\.\d{1,2})?|[1-9]+\d*(\.\d{1,2})?)$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"1"*5000+"!1 __POA(i)"

import re
from time import perf_counter

regex = """^([1-9]+\d{0,2},(\d{3},)*\d{3}(\.\d{1,2})?|[1-9]+\d*(\.\d{1,2})?)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1" * i * 10000 + "!1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")