# 1872
# ^(([a-zA-Z]:)|((\\|/){1,2}\w+)\$?)((\\|/)(\w[\w ]*.*))+\.([a-zA-Z0-9]+)$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+"a:\\1."*32+"!1 _SLQ_2"

import re2 as re
from time import perf_counter

regex = """^(([a-zA-Z]:)|((\\|/){1,2}\w+)\$?)((\\|/)(\w[\w ]*.*))+\.([a-zA-Z0-9]+)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "a:\\1." * i * 1 + "!1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")