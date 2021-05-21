# 2891
# (\d*\.?\d+)\s?(px|em|ex|%|in|cn|mm|pt|pc+)
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"1"*512+"◎@! _1!_1SLQ_1"

import re
from time import perf_counter

regex = """(\d*\.?\d+)\s?(px|em|ex|%|in|cn|mm|pt|pc+)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1" * i * 1 + "◎@! _1!_1SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")