# 4269
# ^(?<Drive>([a-zA-Z]:)|(\\{2}\w+)\$?)(\\(\w[\w].*))(?<Year>\d{4})-(?<Month>\d{1,2})-(?<Day>\d{1,2})(?<ExtraText>.*)(?<Extension>.csv|.CSV)$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"a:\\111111-1-1"*5000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """^(?<Drive>([a-zA-Z]:)|(\\{2}\w+)\$?)(\\(\w[\w].*))(?<Year>\d{4})-(?<Month>\d{1,2})-(?<Day>\d{1,2})(?<ExtraText>.*)(?<Extension>.csv|.CSV)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "a:\\111111-1-1" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")