# 6841
# (?<quote>["]?)(?<param>(?:\k<quote>{2}|[^"]+)*)\k<quote>[ ]+
# EXPONENT
# nums:5
# EXPONENT AttackString:""+" "*16+"!1 __NQ"

import re2 as re
from time import perf_counter

regex = """(?<quote>["]?)(?<param>(?:\k<quote>{2}|[^"]+)*)\k<quote>[ ]+"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "" + " " * i * 1 + "!1 __NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")