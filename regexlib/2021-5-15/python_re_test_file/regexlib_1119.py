# 1119
# (^([0-9]*[.][0-9]*[1-9]+[0-9]*)$)|(^([0-9]*[1-9]+[0-9]*[.][0-9]+)$)|(^([1-9]+[0-9]*)$)
# EXPONENT
# nums:4
# EXPONENT AttackString:".1"+"1"*512+"!1 _SLQ_2"

import re
from time import perf_counter

regex = """(^([0-9]*[.][0-9]*[1-9]+[0-9]*)$)|(^([0-9]*[1-9]+[0-9]*[.][0-9]+)$)|(^([1-9]+[0-9]*)$)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = ".1" + "1" * i * 1 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")