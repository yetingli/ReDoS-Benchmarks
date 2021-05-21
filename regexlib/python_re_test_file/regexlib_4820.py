# 4820
# ([0-9a-zA-Z]+)|([0-9a-zA-Z][0-9a-zA-Z\\s]+[0-9a-zA-Z]+)
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"0"*10000+"SLQ_1"

import re
from time import perf_counter

regex = """([0-9a-zA-Z]+)|([0-9a-zA-Z][0-9a-zA-Z\\s]+[0-9a-zA-Z]+)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0" * i * 10000 + "SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")