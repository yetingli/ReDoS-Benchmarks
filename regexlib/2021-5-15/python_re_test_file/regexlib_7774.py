# 7774
# myInstance\.myMethod(.*)\(.*myParam.*\)
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"myInstance.myMethod(myParam"*128+"! _1SLQ_2"

import re
from time import perf_counter

regex = """myInstance\.myMethod(.*)\(.*myParam.*\)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "myInstance.myMethod(myParam" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")