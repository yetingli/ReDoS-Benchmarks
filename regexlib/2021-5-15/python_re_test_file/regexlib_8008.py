# 8008
# (\[[Ii][Mm][Gg]\])(\S+?)(\[\/[Ii][Mm][Gg]\])
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"[IMG]"*5000+"@1 _SLQ_2"

import re
from time import perf_counter

regex = """(\[[Ii][Mm][Gg]\])(\S+?)(\[\/[Ii][Mm][Gg]\])"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "[IMG]" * i * 10000 + "@1 _SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")