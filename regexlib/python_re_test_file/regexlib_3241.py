# 3241
# <[iI][mM][gG][a-zA-Z0-9\s=".]*((src)=\s*(?:"([^"]*)"|'[^']*'))[a-zA-Z0-9\s=".]*/*>(?:</[iI][mM][gG]>)*
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"<img"+"src="""*5000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """<[iI][mM][gG][a-zA-Z0-9\s=".]*((src)=\s*(?:"([^"]*)"|'[^']*'))[a-zA-Z0-9\s=".]*/*>(?:</[iI][mM][gG]>)*"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "<img" + "src=\"\"" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")