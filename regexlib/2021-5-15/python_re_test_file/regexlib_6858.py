# 6858
# \b[\w]+[\w.-][\w]+@[\w]+[\w.-]\.[\w]{2,4}\b
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"11"*5000+"!1 _SLQ_2"

import re
from time import perf_counter

regex = """\b[\w]+[\w.-][\w]+@[\w]+[\w.-]\.[\w]{2,4}\b"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "11" * i * 10000 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")