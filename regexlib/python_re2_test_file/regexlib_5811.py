# 5811
# ^(?<title>.*\.\s)*(?<firstname>([A-Z][a-z]+\s*)+)(\s)(?<middleinitial>([A-Z]\.?\s)*)(?<lastname>[A-Z][a-zA-Z-']+)(?<suffix>.*)$
# EXPONENT
# nums:5
# EXPONENT AttackString:""+".\t"*32+"! _1_EOA(iii)"

import re2 as re
from time import perf_counter

regex = """^(?<title>.*\.\s)*(?<firstname>([A-Z][a-z]+\s*)+)(\s)(?<middleinitial>([A-Z]\.?\s)*)(?<lastname>[A-Z][a-zA-Z-']+)(?<suffix>.*)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + ".\t" * i * 1 + "! _1_EOA(iii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")