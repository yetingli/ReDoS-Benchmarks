# 8286
# ^((CN=(['\w\d\s\-\&amp;\.]+(\\/)*(\\,)*)+,\s*)*(OU=(['\w\d\s\-\&amp;\.]+(\\/)*(\\,)*)+,\s*)*(DC=['\w\d\s\-\&amp;]+[,]*\s*){1,}(DC=['\w\d\s\-\&amp;]+\s*){1})$
# EXPONENT
# nums:5
# EXPONENT AttackString:"DC='"+"DC=\t\t"*32+"! _1_EOA(i or ii)"

import re2 as re
from time import perf_counter

regex = """^((CN=(['\w\d\s\-\&amp;\.]+(\\/)*(\\,)*)+,\s*)*(OU=(['\w\d\s\-\&amp;\.]+(\\/)*(\\,)*)+,\s*)*(DC=['\w\d\s\-\&amp;]+[,]*\s*){1,}(DC=['\w\d\s\-\&amp;]+\s*){1})$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "DC=\'" + "DC=\t\t" * i * 1 + "! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")