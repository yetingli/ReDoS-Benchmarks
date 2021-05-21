# 4570
# (http(s?)://|[a-zA-Z0-9\-]+\.)[a-zA-Z0-9/~\-]+\.[a-zA-Z0-9/~\-_,&\?\.;]+[^\.,\s<]
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:""+"a"*10000+"◎@! _1!1 _SLQ_1<"

import re
from time import perf_counter

regex = """(http(s?)://|[a-zA-Z0-9\-]+\.)[a-zA-Z0-9/~\-]+\.[a-zA-Z0-9/~\-_,&\?\.;]+[^\.,\s<]"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + "a" * i * 10000 + "◎@! _1!1 _SLQ_1<"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")