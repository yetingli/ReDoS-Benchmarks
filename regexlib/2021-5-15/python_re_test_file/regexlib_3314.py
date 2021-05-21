# 3314
# ^([\u00c0-\u01ffa-zA-Z'\-]+[ ]?[\u00c0-\u01ffa-zA-Z'\-]*)+$
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"''"*8+"!1 __EOA(i or ii)"

import re
from time import perf_counter

regex = """^([\u00c0-\u01ffa-zA-Z'\-]+[ ]?[\u00c0-\u01ffa-zA-Z'\-]*)+$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "\'\'" * i * 1 + "!1 __EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")