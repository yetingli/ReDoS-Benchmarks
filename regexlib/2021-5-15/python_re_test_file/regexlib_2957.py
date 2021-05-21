# 2957
# \w+[\w-\.]*\@\w+((-\w+)|(\w*))\.[a-z]{2,3}$|^([0-9a-zA-Z'\.]{3,40})\*|([0-9a-zA-Z'\.]+)@([0-9a-zA-Z']+)\.([0-9a-zA-Z']+)$|([0-9a-zA-Z'\.]+)@([0-9a-zA-Z']+)\*+$|^$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"1@1"+"-1"*10000+"! _1SLQ_2"

import re
from time import perf_counter

regex = """\w+[\w-\.]*\@\w+((-\w+)|(\w*))\.[a-z]{2,3}$|^([0-9a-zA-Z'\.]{3,40})\*|([0-9a-zA-Z'\.]+)@([0-9a-zA-Z']+)\.([0-9a-zA-Z']+)$|([0-9a-zA-Z'\.]+)@([0-9a-zA-Z']+)\*+$|^$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1@1" + "-1" * i * 10000 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")