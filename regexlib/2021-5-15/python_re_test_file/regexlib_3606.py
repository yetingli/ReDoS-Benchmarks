# 3606
# ^(\w+)s?[:]\/\/(\w+)?[.]?(\w+)[.](\w+)$
# POLYNOMIAL
# nums:4
# POLYNOMIAL AttackString:"1://"+"0"*10000+"! _1_POA(i)"

import re
from time import perf_counter

regex = """^(\w+)s?[:]\/\/(\w+)?[.]?(\w+)[.](\w+)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "1://" + "0" * i * 10000 + "! _1_POA(i)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *10000}: took {DURATION} seconds!")