# 7128
# ^(9|2{1})+([1-9]{1})+([0-9]{7})$
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"9"*5000+"!1 _!1 _! _1!\n_SLQ_3"

import re2 as re
from time import perf_counter

regex = """^(9|2{1})+([1-9]{1})+([0-9]{7})$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "9" * i * 10000 + "!1 _!1 _! _1!\n_SLQ_3"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")