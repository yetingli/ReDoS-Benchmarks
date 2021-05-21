# 2354
# ^(NAME)(\s?)<?(\w*)(\s*)([0-9]*)>?$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"NAME"+"0"*10000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """^(NAME)(\s?)<?(\w*)(\s*)([0-9]*)>?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "NAME" + "0" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")