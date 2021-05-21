# 2758
# ^[\s]*(?:(Public|Private)[\s]+(?:[_][\s]*[\n\r]+)?)?(Function|Sub)[\s]+(?:[_][\s]*[\n\r]+)?([a-zA-Z][\w]{0,254})(?:[\s\n\r_]*\((?:[\s\n\r_]*([a-zA-Z][\w]{0,254})[,]?[\s]*)*\))?
# EXPONENT
# nums:5
# EXPONENT AttackString:"Function a("+"\tA"*32+"!1 __EOA(i or ii)"

import re2 as re
from time import perf_counter

regex = """^[\s]*(?:(Public|Private)[\s]+(?:[_][\s]*[\n\r]+)?)?(Function|Sub)[\s]+(?:[_][\s]*[\n\r]+)?([a-zA-Z][\w]{0,254})(?:[\s\n\r_]*\((?:[\s\n\r_]*([a-zA-Z][\w]{0,254})[,]?[\s]*)*\))?"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "Function a(" + "\tA" * i * 1 + "!1 __EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")