# 229
# (\+1|1)?[ \-\.]?\(?(?<areacode>[0-9]{3})\)?[ \-\.]?(?<prefix>[0-9]{3})[ \-\.]?(?<number>[0-9]{4})[ \.]*(ext|x)?[ \.]*(?<extension>[0-9]{0,5})
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"0000000000"+" "*10000+"◎@! _1_POA(i)"

import re
from time import perf_counter

regex = """(\+1|1)?[ \-\.]?\(?(?<areacode>[0-9]{3})\)?[ \-\.]?(?<prefix>[0-9]{3})[ \-\.]?(?<number>[0-9]{4})[ \.]*(ext|x)?[ \.]*(?<extension>[0-9]{0,5})"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "0000000000" + " " * i * 10000 + "◎@! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")