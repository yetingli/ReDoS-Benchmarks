# 264
# ((^[0-9]*).?((BIS)|(TER)|(QUATER))?)?((\W+)|(^))(([a-z]+.)*)([0-9]{5})?.(([a-z\'']+.)*)$
# EXPONENT
# nums:4
# EXPONENT AttackString:"'"+"a"*32+"!1 __EOA(iv)"

import re
from time import perf_counter

regex = """((^[0-9]*).?((BIS)|(TER)|(QUATER))?)?((\W+)|(^))(([a-z]+.)*)([0-9]{5})?.(([a-z\'']+.)*)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "\'" + "a" * i * 1 + "!1 __EOA(iv)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")