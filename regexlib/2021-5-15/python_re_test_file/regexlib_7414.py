# 7414
# ^[\u0600-\u06ff\s]+$|[\u0750-\u077f\s]+$|[\ufb50-\ufc3f\s]+$|[\ufe70-\ufefc\s]+$|^$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"ݿ"*20000+"!1 _SLQ_1"

import re
from time import perf_counter

regex = """^[\u0600-\u06ff\s]+$|[\u0750-\u077f\s]+$|[\ufb50-\ufc3f\s]+$|[\ufe70-\ufefc\s]+$|^$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "ݿ" * i * 10000 + "!1 _SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")