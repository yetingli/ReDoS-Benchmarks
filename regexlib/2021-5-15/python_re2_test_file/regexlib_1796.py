# 1796
# target[ ]*[=]([ ]*)([&quot;]|['])*([_])*([A-Za-z0-9])+([&quot;])*
# EXPONENT
# nums:5
# EXPONENT AttackString:"target="+"o"*1024+"!1 _!1 _!1 _! _1!\n_SLQ_3"

import re2 as re
from time import perf_counter

regex = """target[ ]*[=]([ ]*)([&quot;]|['])*([_])*([A-Za-z0-9])+([&quot;])*"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "target=" + "o" * i * 1 + "!1 _!1 _!1 _! _1!\n_SLQ_3"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")