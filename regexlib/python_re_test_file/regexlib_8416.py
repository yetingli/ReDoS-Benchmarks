# 8416
# (^[1]$)|(^[1]+\d*\.+\d*[1-5]$)
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"1"+"1"*10000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """(^[1]$)|(^[1]+\d*\.+\d*[1-5]$)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1" + "1" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")