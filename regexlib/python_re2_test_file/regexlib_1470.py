# 1470
# \[link="(?<link>((.|\n)*?))"\](?<text>((.|\n)*?))\[\/link\]
# POLYNOMIAL
# nums:5
# POLYNOMIAL AttackString:"[link=""+""]"*5000+"◎@! _1_POA(i)"

import re2 as re
from time import perf_counter

regex = """\[link="(?<link>((.|\n)*?))"\](?<text>((.|\n)*?))\[\/link\]"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "[link=\"" + "\"]" * i * 10000 + "◎@! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")