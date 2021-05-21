# 248
# ^([A-Za-z]+)([0-9]+)?([A-Za-z0-9\.\_]+)?\@(([A-Za-z]+)([0-9]+)?([A-Za-z0-9\.\_]+)?)((\.)([a-zA-Z]+))$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"A"*10000+"!1 __POA(i)"

import re
from time import perf_counter

regex = """^([A-Za-z]+)([0-9]+)?([A-Za-z0-9\.\_]+)?\@(([A-Za-z]+)([0-9]+)?([A-Za-z0-9\.\_]+)?)((\.)([a-zA-Z]+))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "A" * i * 10000 + "!1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")