# 1141
# ^[-+]?[0-9]+[.]?[0-9]*([eE][-+]?[0-9]+)?$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"0"*10000+"!1 _SLQ_2"

import re
from time import perf_counter

regex = """^[-+]?[0-9]+[.]?[0-9]*([eE][-+]?[0-9]+)?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "0" * i * 10000 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")