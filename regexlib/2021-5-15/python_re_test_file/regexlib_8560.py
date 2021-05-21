# 8560
# ^((([-+]?(\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?[r]?))|(([-+]?((\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?)?[i]))|(([-+]?(\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?[r]?))(([-+]((\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?)?[i])))$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"1"*5000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """^((([-+]?(\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?[r]?))|(([-+]?((\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?)?[i]))|(([-+]?(\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?[r]?))(([-+]((\d+\.?\d*|\d*\.?\d+)([Ee][-+]?[0-2]?\d{1,2})?)?[i])))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "1" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")