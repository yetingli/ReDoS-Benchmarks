# 8010
# (\S*)+(\u007C)+(\S*)
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"|"*32+"@1 _SLQ_2!"

import re
from time import perf_counter

regex = """(\S*)+(\u007C)+(\S*)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "|" * i * 1 + "@1 _SLQ_2!"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")