# 5784
# [a-zA-Z]{3,}://[a-zA-Z0-9\.]+/*[a-zA-Z0-9/\\%_.]*\?*[a-zA-Z0-9/\\%_.=&amp;]*
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"aaa"*5000+"! _1SLQ_1"

import re2 as re
from time import perf_counter

regex = """[a-zA-Z]{3,}://[a-zA-Z0-9\.]+/*[a-zA-Z0-9/\\%_.]*\?*[a-zA-Z0-9/\\%_.=&amp;]*"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "aaa" * i * 10000 + "! _1SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")