# 3647
# ^/{1}(((/{1}\.{1})?[a-zA-Z0-9 ]+/?)+(\.{1}[a-zA-Z0-9]{2,4})?)$
# EXPONENT
# nums:5
# EXPONENT AttackString:"/"+"a"*32+"◎@! _1_NQ"

import re2 as re
from time import perf_counter

regex = """^/{1}(((/{1}\.{1})?[a-zA-Z0-9 ]+/?)+(\.{1}[a-zA-Z0-9]{2,4})?)$"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "/" + "a" * i * 1 + "◎@! _1_NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")