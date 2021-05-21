# 8266
# ^(?i:([a-z0-9!#$%^&*{}'`+=-_|/?]+(?:\.[a-z0-9!#$%^&*{}'`+=-_|/?]+)*)@([a-z0-9]+\z?.*[a-z0-9-_]+)*(\.[a-z0-9]{2,}))$
# EXPONENT
# nums:4
# EXPONENT AttackString:"ia@"+"a"*16+"! _1SLQ_2"

import re
from time import perf_counter

regex = """^(?i:([a-z0-9!#$%^&*{}'`+=-_|/?]+(?:\.[a-z0-9!#$%^&*{}'`+=-_|/?]+)*)@([a-z0-9]+\z?.*[a-z0-9-_]+)*(\.[a-z0-9]{2,}))$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "ia@" + "a" * i * 1 + "! _1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")