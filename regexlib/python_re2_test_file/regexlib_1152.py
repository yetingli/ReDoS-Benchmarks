# 1152
# (<(tag1|tag2)[^>]*\/?>)[\w\S\s]*?(<\/(?:\2)>)
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"<tag1>"*5000+"@1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """(<(tag1|tag2)[^>]*\/?>)[\w\S\s]*?(<\/(?:\2)>)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "<tag1>" * i * 10000 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")