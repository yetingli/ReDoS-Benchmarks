# 8255
# ^[\u0600-\u06ff0-9\s]+$|[\u0750-\u077f0-9\s]+$|[\ufb50-\ufc3f0-9\s]+$|[\ufe70-\ufefc0-9\s]+$|[\u06cc0-9\s]+$|[\u067e0-9\s]+$|[\u06af0-9\s]$|[\u06910-9\s]+$|^$
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:""+"ݿ"*10000+"!1 _SLQ_1"

import re2 as re
from time import perf_counter

regex = """^[\u0600-\u06ff0-9\s]+$|[\u0750-\u077f0-9\s]+$|[\ufb50-\ufc3f0-9\s]+$|[\ufe70-\ufefc0-9\s]+$|[\u06cc0-9\s]+$|[\u067e0-9\s]+$|[\u06af0-9\s]$|[\u06910-9\s]+$|^$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "ݿ" * i * 10000 + "!1 _SLQ_1"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")