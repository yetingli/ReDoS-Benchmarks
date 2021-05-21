# 3374
# ^([A-Z]{3,20}\s?[A-Z]{2}[0-9]{1,3}-([A-Z]{3}|[A-Z]{1}[0-9]{2}))|([A-Z]{1,20}\s[A-Z]{1,2}[0-9]{1,4}-[A-Z]{1,3})|([\d,\w,\s]{1,20}\s[A-Z]{3}-[0-9]{1,3})|([A-Z]{1,20}\s?[\d,\w,\s]{1,20})$
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"A"*80000+"!_1SLQ_1"

import re2 as re
from time import perf_counter

regex = """^([A-Z]{3,20}\s?[A-Z]{2}[0-9]{1,3}-([A-Z]{3}|[A-Z]{1}[0-9]{2}))|([A-Z]{1,20}\s[A-Z]{1,2}[0-9]{1,4}-[A-Z]{1,3})|([\d,\w,\s]{1,20}\s[A-Z]{3}-[0-9]{1,3})|([A-Z]{1,20}\s?[\d,\w,\s]{1,20})$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "A" * i * 10000 + "!_1SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")