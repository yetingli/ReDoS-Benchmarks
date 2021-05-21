# 277
# (\+)?([-\._\(\) ]?[\d]{3,20}[-\._\(\) ]?){2,10}
# EXPONENT
# nums:4
# EXPONENT AttackString:"111111"+"111"*16+"◎@! _1_NQ"

import re
from time import perf_counter

regex = """(\+)?([-\._\(\) ]?[\d]{3,20}[-\._\(\) ]?){2,10}"""
REGEX = re.compile(regex)
for i in range(0, 150000):
    ATTACK = "111111" + "111" * i * 1 + "◎@! _1_NQ"
    LEN = len(ATTACK)
    BEGIN = perf_counter()
    m = REGEX.search(ATTACK)
    # m = REGEX.match(ATTACK)
    DURATION = perf_counter() - BEGIN
    print(f"{i *1}: took {DURATION} seconds!")