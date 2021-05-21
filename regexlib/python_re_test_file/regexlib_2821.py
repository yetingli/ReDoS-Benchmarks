# 2821
# &quot;([^&quot;](?:\\.|[^\\&quot;]*)*)&quot;
# EXPONENT
# nums:4
# EXPONENT AttackString:"&quot;:"+":"*16+"! _1_NQ"

import re
from time import perf_counter

regex = """&quot;([^&quot;](?:\\.|[^\\&quot;]*)*)&quot;"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "&quot;:" + ":" * i * 1 + "! _1_NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")