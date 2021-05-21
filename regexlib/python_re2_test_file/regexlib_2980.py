# 2980
# (\s+|)((\(\d{3}\) +)|(\d{3}-)|(\d{3} +))?\d{3}(-| +)\d{4}( +x\d{1,4})?(\s+|)
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+" "*5000+"!_1◎@! _1SLQ_1"

import re2 as re
from time import perf_counter

regex = """(\s+|)((\(\d{3}\) +)|(\d{3}-)|(\d{3} +))?\d{3}(-| +)\d{4}( +x\d{1,4})?(\s+|)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + " " * i * 10000 + "!_1◎@! _1SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")