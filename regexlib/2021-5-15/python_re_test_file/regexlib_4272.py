# 4272
# ^(((\.\.){1}/)*|(/){1})?(([a-zA-Z0-9]*)/)*([a-zA-Z0-9]*)+([.jpg]|[.gif])+$
# EXPONENT
# nums:4
# EXPONENT AttackString:""+"f"*32+"!1 _!\n_SLQ_3"

import re
from time import perf_counter

regex = """^(((\.\.){1}/)*|(/){1})?(([a-zA-Z0-9]*)/)*([a-zA-Z0-9]*)+([.jpg]|[.gif])+$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "f" * i * 1 + "!1 _!\n_SLQ_3"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")