# 7761
# ^[ \w\.]{3,}([A-Za-z]\.)?([ \w]*\##\d+)?(\r\n| )[ \w]{3,},\x20([A-Z]{2}\.)\x20\d{5}(-\d{4})?$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"   "*5000+"!1 __POA(i)"

import re
from time import perf_counter

regex = """^[ \w\.]{3,}([A-Za-z]\.)?([ \w]*\##\d+)?(\r\n| )[ \w]{3,},\x20([A-Z]{2}\.)\x20\d{5}(-\d{4})?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "   " * i * 10000 + "!1 __POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")