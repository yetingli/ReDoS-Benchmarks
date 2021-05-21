# 3603
# [\d+]{10}\@[\w]+\.?[\w]+?\.?[\w]+?\.?[\w+]{2,4}/i
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"1111111111@1"*80000+"!1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """[\d+]{10}\@[\w]+\.?[\w]+?\.?[\w]+?\.?[\w+]{2,4}/i"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1111111111@1" * i * 10000 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")