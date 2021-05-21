# 6637
# [p|P][\s]*[o|O][\s]*[b|B][\s]*[o|O][\s]*[x|X][\s]*[a-zA-Z0-9]*|\b[P|p]+(OST|ost|o|O)?\.?\s*[O|o|0]+(ffice|FFICE)?\.?\s*[B|b][O|o|0]?[X|x]+\.?\s+[#]?(\d+)*(\D+)*\b
# EXPONENT
# nums:5
# EXPONENT AttackString:"POBX "+"0"*32+"!1 __NQ"

import re2 as re
from time import perf_counter

regex = """[p|P][\s]*[o|O][\s]*[b|B][\s]*[o|O][\s]*[x|X][\s]*[a-zA-Z0-9]*|\b[P|p]+(OST|ost|o|O)?\.?\s*[O|o|0]+(ffice|FFICE)?\.?\s*[B|b][O|o|0]?[X|x]+\.?\s+[#]?(\d+)*(\D+)*\b"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "POBX " + "0" * i * 1 + "!1 __NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")