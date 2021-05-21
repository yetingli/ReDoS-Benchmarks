# 8007
# ^[\.\w&#230;&#248;&#229;-]+@([a-z&#230;&#248;&#229;0-9]+([\.-]{0,1}[a-z&#230;&#248;&#229;0-9]+|[a-z&#230;&#248;&#229;0-9]?))+\.[a-z]{2,6}$
# EXPONENT
# nums:5
# EXPONENT AttackString:".@"+"&"*16+"!1 __EOA(iii)"

import re2 as re
from time import perf_counter

regex = """^[\.\w&#230;&#248;&#229;-]+@([a-z&#230;&#248;&#229;0-9]+([\.-]{0,1}[a-z&#230;&#248;&#229;0-9]+|[a-z&#230;&#248;&#229;0-9]?))+\.[a-z]{2,6}$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = ".@" + "&" * i * 1 + "!1 __EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")