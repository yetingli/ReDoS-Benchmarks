# 3428
# (\/\*(\s*|.*?)*\*\/)|(\/\/.*)
# EXPONENT
# nums:5
# EXPONENT AttackString:"/*"+"1"*16+"◎@! _1_NQ"

import re2 as re
from time import perf_counter

regex = """(\/\*(\s*|.*?)*\*\/)|(\/\/.*)"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "/*" + "1" * i * 1 + "◎@! _1_NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")