# 1726
# class\s+([a-z0-9_]+)(?:\s+extends\s+[a-z0-9_]+)?(?:\s+implements\s+(?:[a-z0-9_]+\s*,*\s*)+)?\s*\{
# EXPONENT
# nums:4
# EXPONENT AttackString:"class a"+" implements"*4+"!_1SLQ_2"

import re
from time import perf_counter

regex = """class\s+([a-z0-9_]+)(?:\s+extends\s+[a-z0-9_]+)?(?:\s+implements\s+(?:[a-z0-9_]+\s*,*\s*)+)?\s*\{"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "class a" + " implements" * i * 1 + "!_1SLQ_2"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")